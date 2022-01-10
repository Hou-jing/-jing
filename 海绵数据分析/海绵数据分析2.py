import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
fm.rcParams['font.family']=['SimHei']
prince_trial = 'https://media-zip1.baydn.com/storage_media_zip/qkklny/7e8e1941cb36ad97cbaa6eed0dff441e.cd58f0dcbe18f95e2b1912dbd63a4e67.csv'
df = pd.read_csv(prince_trial)
print(df.head(3))
#分析阅读时间和购买之间的关键
under_30=df[df['time_stay']<=30]
above_30=df[df['time_stay']>30]
under_30_pay=under_30[under_30['pay']]
above_30_pay=above_30[above_30['pay']]
num_under_30=len(under_30)
num_above_30=len(above_30)
num_above_30_pay=len(above_30_pay)
num_under_30_pay=len(under_30_pay)
ratio_above_30_pay=num_above_30_pay/num_above_30
ratio_under_30_pay=num_under_30_pay/num_under_30
print(ratio_under_30_pay,ratio_above_30_pay)
labels = ['Not Interested', 'Don\'t Understand', 'Both', 'Neither']
data = [138, 792, 113, 124]
plt.pie(data,explode=(0,0.1,0,0),labels=labels,autopct='%0.1f%%')
plt.show()

'''
#分析阅读时间与阅读下一页的比例
plt.hist(df['time_stay'],bins=10,facecolor='blue',edgecolor='black')
plt.xlabel('time stay')
plt.ylabel('number of users')
# plt.show()
# df_time=pd.cut(df['time_stay'],bins=[0,30,60],labels=['小于30秒','大于30秒'])
# df['时间类别']=df_time
# print(df.head(3))
# df_group_time=df.groupby('时间类别')
# print(df_group_time['时间类别'].value_counts())
under_30=df[df['time_stay']<=30]
above_30=df[df['time_stay']>30]
next_under_30=under_30['next_page'].value_counts()
next_above_30=above_30['next_page'].value_counts()
# print(len(above_30[above_30['next_page']]))
print(next_under_30,next_above_30)
print('试读不超过30s',next_under_30/len(under_30))
print('试读超过30s',next_above_30/len(above_30))
#选择点击下一页的概率
# T_F=next_under_30/len(under_30)
# print(T_F[1])
'''

'''
整体流程：
绘制分组柱状图，对比 AB 测试的两组漏斗；
利用 pandas 中的布尔索引筛选符合条件的数据记录；
用直方图来研究数据分布，并根据分布将数据进行进一步分组研究；
通过产品内问卷的方法，验证对用户行为动机的判断。'''