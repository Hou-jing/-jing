import json

import accelerate
import numpy as np
import torch.nn as nn
import torch
import transformers
import torch.optim as optim
from tqdm import tqdm
import time
from transformers import AdamW,BertTokenizer,BertModel
model_name='bert-base-chinese'
bert_model=BertModel.from_pretrained(model_name)
chi_tokenizer=BertTokenizer.from_pretrained(model_name)
start_time=time.time()
id2rel={0: 'UNK', 1: '主演', 2: '歌手', 3: '简称', 4: '总部地点', 5: '导演', 6: '出生地', 7: '目', 8: '出生日期', 9: '占地面积', 10: '上映时间', 11: '出版社', 12: '作者', 13: '号', 14: '父亲', 15: '毕业院校', 16: '成立日期', 17: '改编自', 18: '主持人', 19: '所属专辑', 20: '连载网站', 21: '作词', 22: '作曲', 23: '创始人', 24: '丈夫', 25: '妻子', 26: '朝代', 27: '民族', 28: '国籍', 29: '身高', 30: '出品公司', 31: '母亲', 32: '编剧', 33: '首都', 34: '面积', 35: '祖籍', 36: '嘉宾', 37: '字', 38: '海拔', 39: '注册资本', 40: '制片人', 41: '董事长', 42: '所在城市', 43: '气候', 44: '人口数量', 45: '邮政编码', 46: '主角', 47: '官方语言', 48: '修业年限'}
rel2id={v:k for k,v in id2rel.items()}
# def read_file():
#     with open('./train.json', encoding='utf_8') as f:
#         sentence=[]
#         labels=[]
#         for line in f:
#             line=json.loads(line)
#             sent=line['ent1']+line['ent2']+line['text']
#             label=line['rel']
#             if label not in rel2id.keys():
#                 labels.append(0)
#             else:
#                 labels.append(rel2id[label])
#             sentence.append(sent)
#     return sentence,labels
# def encode(sents):
#     inputs=chi_tokenizer(sents,return_tensors='pt',padding=True)
#     return inputs
def load_train():
    max_length=128
    tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')
    train_data = {}
    train_data['label'] = []
    train_data['mask'] = []
    train_data['text'] = []

    with open("./train.json", 'r', encoding='utf-8') as load_f:
        temp = load_f.readlines()
        temp = temp[:3000]
        for line in temp:
            dic = json.loads(line)
            if dic['rel'] not in rel2id:
                train_data['label'].append(0)
            else:
                train_data['label'].append(rel2id[dic['rel']])
            sent=dic['ent1']+dic['ent2']+dic['text']
            indexed_tokens = tokenizer.encode(sent, add_special_tokens=True)
            avai_len = len(indexed_tokens)
            while len(indexed_tokens) <  max_length:
                indexed_tokens.append(0)  # 0 is id for [PAD]
            indexed_tokens = indexed_tokens[: max_length]
            indexed_tokens = torch.tensor(indexed_tokens).long().unsqueeze(0)  # (1, L)

            # Attention mask
            att_mask = torch.zeros(indexed_tokens.size()).long()  # (1, L)
            att_mask[0, :avai_len] = 1
            train_data['text'].append(indexed_tokens)
            train_data['mask'].append(att_mask)
    return train_data

data=load_train()
train_text=data['text']
train_mask=data['mask']
train_label=data['label']
train_text = [ t.numpy() for t in train_text]
train_mask = [ t.numpy() for t in train_mask]
train_text=torch.tensor(train_text)
train_mask=torch.tensor(train_mask)
train_label=torch.tensor(train_label)
print(train_text.shape,train_label.shape,train_mask.shape)
train_dataset = torch.utils.data.TensorDataset(train_text,train_mask,train_label)
class classifier(nn.Module):
    def __init__(self):
        super(classifier, self).__init__()
        self.encode=BertModel.from_pretrained('bert-base-chinese')
        self.dropout=nn.Dropout(0.1)
        self.fc1=nn.Linear(768,128)
        self.relu=nn.ReLU()
        self.fc2=nn.Linear(128,len(rel2id))
    def forward(self,x,mask):
        x=self.encode(x,mask)[0]
        x=x[:,0,:]
        x=self.dropout(x)
        x=self.fc1(x)
        x=self.relu(x)
        x=self.fc2(x)
        return x
from torch.utils.data import DataLoader,Dataset
import torch.nn as nn
# device='cuda' if torch.cuda.is_available() else 'gpu'

from accelerate import Accelerator
accelerator=Accelerator()
device=accelerator.device

# y=torch.tensor(labels,dtype=float)
from torch.utils.data import DataLoader, Dataset, TensorDataset

import torch.nn as nn

train_set=TensorDataset(train_text,train_mask,train_label)
train_loader=DataLoader(train_set,batch_size=4,shuffle=True)


class YT_Model(nn.Module):
    def __init__(self):
        super(YT_Model, self).__init__()
        self.encode = BertModel.from_pretrained('bert-base-chinese')
        self.dropout = nn.Dropout(0.1)
        self.fc1 = nn.Linear(768, 128)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(128, len(rel2id))

    def forward(self, x, mask):
        x = self.encode(x, mask)[0]
        x = x[:, 0, :]
        x = self.dropout(x)
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

model=YT_Model()
# model=model.to(device)

lr=1e-3
criterier=torch.nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(model.parameters(),lr)
model, optimizer, train_loader = accelerator.prepare(model,optimizer,train_loader)

def train(net,dataset,num_epochs, learning_rate,  batch_size):
    i=1
    print('执行次数为：{}'.format(i))
    # net=net.to(device)
    net.train()
    optimizer = optim.SGD(net.parameters(), lr=learning_rate,weight_decay=0)
    criterier=nn.CrossEntropyLoss()
    train_loader = torch.utils.data.DataLoader(dataset, batch_size, shuffle=True)

    for epoch in range(num_epochs):
        logging_step=100
        step=1
        train_loss, train_acc = 0, 0
        accum_iter=4
        for batch_idx,data in enumerate(tqdm(train_loader)):
            text,mask,label=data
            text,mask,label=text.to(device),mask.to(device),label.to(device)
            optimizer.zero_grad()
            # with torch.set_grad_enabled(True):
            pre = net(text.squeeze(1), mask.squeeze(1))#text,mask要是（batch_size,sequence_
            loss = criterier(pre, label)
            # loss = loss / accum_iter
            # loss.backward(retain_graph=True)
            accelerator.backward(loss)
            # if ((batch_idx + 1) % accum_iter == 0) or (batch_idx + 1 == len(train_loader)):
            optimizer.step()
            # optimizer.zero_grad()
            pre=pre.argmax(-1)
            train_acc += (pre.cpu() == label.cpu()).sum().item()
            train_loss += loss.item()
            step+=1
            if step%logging_step==0:
              print(
                f"Epoch {epoch + 1} | Step {step} | loss = {train_loss / logging_step:.3f}, acc = {train_acc / (4*logging_step):.3f}")
              train_loss = train_acc = 0
train(model,train_set,5,1e-3,4)
end_time=time.time()
print('total_time',start_time-end_time)
