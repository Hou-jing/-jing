import pandas as pd
import matplotlib.pyplot as plt
#查词功能上线后分析用户行为
df = pd.read_csv('https://media-zip1.baydn.com/storage_media_zip/qkklny/cdef8ac11cea09425c9a5ca1327b6b90.78492cd0c25f0a9a5de36b7534893657.csv')
print(df.head(3))
plt.hist(x=df['time_stay'],edgecolor='black')
plt.show()
print(df['pay'].value_counts()[1])
print('购买比例',df['pay'].value_counts()[1]/len(df['pay']))
df_timelabel=pd.cut(df['time_stay'],bins=[0,30,60,df['time_stay'].max()],labels=['under_30','between_30_60','above_60'])
df['time_label']=df_timelabel
time_under_30=df[df['time_label']=='under_30']
time_between_30_60=df[df['time_label']=='between_30_60']
time_above_60=df[df['time_label']=='above_60']
print('三个时间段的用户比例是 ,',
      len(time_under_30)/len(df),len(time_between_30_60)/len(df),len(time_above_60)/len(df))
plt.pie(x=[len(time_under_30),len(time_between_30_60),len(time_above_60)],labels=['低于30','30-60之间','60以上'])
print('阅读时间再30s以下购买的比例',len(time_under_30[time_under_30['pay']])/len(time_under_30))
print('阅读时间再30-60之间购买的比例',len(time_between_30_60[time_between_30_60['pay']])/len(time_between_30_60))
print('阅读时间再60以上购买的比例',len(time_above_60[time_above_60['pay']])/len(time_above_60))
plt.show()