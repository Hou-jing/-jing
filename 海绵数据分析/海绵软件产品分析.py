import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
fm.rcParams['font.family']=['SimHei']
active_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/22f0e6eaefcfb277176d59e8125cf505.f75f6a24bf8052409e4a0ca5b52c951a.csv')
enterbook_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/aa3af5c54faea4567e02056fb96f0d09.d6312693cb816c2454eba79e46d9ba8c.csv')
trial_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/91b8b8a4df4f78b7ebae222cef306f9a.5a61749229d5f45c8a3336815ab0552c.csv')
paid_uids = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/8e25e9bffcce021c90335ec6900efb4b.28080b0032a0f39617346f4eead7f548.csv')
print('活跃用户ID',active_uids[:10])
print(len(active_uids),len(enterbook_uids),len(trial_uids),len(paid_uids))
print(type(trial_uids))
paid_with_trial_uids =set(paid_uids).intersection(set(trial_uids))
num_paid_with_trial_uids =len(paid_with_trial_uids)#先试读在购书的用户人数
paid_without_trial_uids=set(paid_uids)-paid_with_trial_uids
num_paid_without_trial_uids=len(paid_without_trial_uids)
#分析路径一：用户进入书籍页面-试读书籍-试读后购买
data_trial=[len(enterbook_uids),len(trial_uids),num_paid_with_trial_uids]
plt.bar(x=['进入人数','试读人数','试读后购买人数'],height=data_trial)

#进入书籍页面-直接购买
plt.bar(x=['进入人数','直接购买人数'],height=[len(enterbook_uids),num_paid_without_trial_uids])
plt.show()

active_uids_A = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/4b656482b421cf8b7fe1320f33a11366.0f9ce2db4545294838c80f03bd1cc748.csv')
enterbook_uids_A = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/509ccfddd9527cc94754747fd39cbdd1.898797608e8ea3b0effd3fd8cad55c97.csv')
trial_uids_A = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/265bbd609edcf2285e88e4ab2bf7543c.68864954d8f79cbfbba24e7dad149948.csv')
paid_uids_A = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/3bffb08b0a96eeae9a09ecf9f7f32cce.7d638e84fea03325ced8c19d6efd7c5e.csv')

active_uids_B = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/c40f6b08d77a11349b69d06e2ca19d58.3578e85cdc7b1db8b1d240ae5a2ac86b.csv')
enterbook_uids_B = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/46a3c26c42c91b1d91ea932c375982de.92fc2cb19ade30aaa8b98ecc1ed2856f.csv')
paid_uids_B = np.genfromtxt('https://media-zip1.baydn.com/storage_media_zip/qkklny/0a7e5bc8e4cad60375afa9e6b6ced0c8.a8ae7b8063542ee3efe8a66c00c97b9e.csv')
print('A组数据\n----------')
print('活跃用户数{}\n打开书籍页面用户数{}\n试读用户数{}\n购书用户数{}'.format(len(active_uids_A),
                                                      len(enterbook_uids_A),len(trial_uids_A),len(paid_uids_A)))
print('B组数据\n------------')
print('活跃用户数{}\n打开书籍页面用户数{}\n购书用户数{}'.format(len(active_uids_B),len(enterbook_uids_B),len(paid_uids_B)))
labels=['打开页面用户数','试读用户数','购书用户数']
x=np.arange(len(labels))
width=0.35
plt.bar(x=x-width/2,height=[len(enterbook_uids_A),len(trial_uids_A),len(paid_uids_A)],label='A')
plt.bar(x=x+width/2,height=[len(enterbook_uids_B),0,len(paid_uids_B)],label='B')
plt.xticks(x,labels)
plt.legend()
plt.show()