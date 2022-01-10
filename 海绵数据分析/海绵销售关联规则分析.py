import pandas as pd
from mlxtend import preprocessing
import numpy as np
from mlxtend.frequent_patterns import apriori,association_rules
encoder=preprocessing.TransactionEncoder()
df=np.genfromtxt(
    'https://media-zip1.baydn.com/storage_media_zip/qkklny/a77f0c6443b6f5594b8f80d4aa7dfed1.42db6c0445109c28f3e3b9ad444e1ea6.csv',
    encoding='utf_8',
    delimiter=',',
    dtype=None,
    skip_header=True
)
print(df[:3])
#处理空数据
data=[]
for line in df:
    newline=[]
    for i in line:
        if i !='':
            newline.append(i)
            data.append(newline)
encoder_data=encoder.fit(data)
one_hot_array=encoder_data.transform(data)
column_label=encoder_data.columns_
print(column_label)
df2=pd.DataFrame(one_hot_array,columns=encoder_data.columns_)
support_rule=apriori(df2,min_support=0.4,use_colnames=True)
lift_rule=association_rules(support_rule,metric='lift',min_threshold=0.8)
df3=lift_rule.sort_values('confidence',ascending=False)
print(df3.head(5))
df3.to_csv('书籍关联规则.csv')
