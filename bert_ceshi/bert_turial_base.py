'''
import torch
from transformers import BertModel,BertTokenizer
model_name='bert-base-chinese'
tokenizer=BertTokenizer.from_pretrained(model_name)
model=BertModel.from_pretrained(model_name)
sent=['小红今天要来上课吗','欧文以为今晚放假']
inputs=tokenizer(sent,return_tensors='pt',padding=True,add_special_tokens=True,max_length=12)
input_id=inputs['input_ids']
att_mask=inputs['attention_mask']


print(input_id,att_mask)
print(input_id.shape,att_mask.shape)
output=model(input_id,att_mask)
print(output)
print(output[0])
print(output[0].shape)
hidden_layer=output[0]
import torch.nn as nn
linear=nn.Linear(768,128)
line=linear(output[0])
print(line)
print(line.shape)
'''
# bert使用时，千万不能直接吧bert-encode的向量作为数据，会爆炸的
# 一般是吧inputid，mask作为数据源




#Cross_entropy loss 函数用法
# (target不需要是onehot 向量，【batch】)
# data的维度是【batch-size，sequence length
import torch
from torch.nn import CrossEntropyLoss
loss=CrossEntropyLoss()
label=torch.Tensor([1,2,4,5]).long()
# label=torch.tensor([[0,0,0,1],[0,0,1,0],[0,0,0,1],[0,1,0,0]]).long()#RuntimeError: 0D or 1D target tensor expected, multi-target not supported
data=torch.randn((4,10))
print(type(data),type(label),data.shape,label.shape)
print('tensor的dtype为：',data.dtype,label.dtype)

criter=loss(data,label)
print(criter)