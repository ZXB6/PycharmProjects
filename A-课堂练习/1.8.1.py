import numpy as np
import pandas as pd

df1 = pd.DataFrame(pd.read_csv('手机数据表1.csv'))
df2 = pd.DataFrame(pd.read_excel('手机数据表2.xlsx'))

ave_price = df1['价格/元'].mean()
df1= df1.fillna(ave_price)
df1['价格/元'] =df1['价格/元'] .astype('int')
df1['品牌'] =df1['品牌'].replace('HW','HUAWEI')
df1['品牌'] =df1['品牌'].str.upper()
print(df2)
df_inner = pd.merge(df1,df2,how='inner')

df_inner = df_inner.set_index('编号')
df_inner = df_inner.sort_index()
# print( df_inner)
df_split = pd.DataFrame((x.split('-') for x in df_inner['配置/GB']),
                            index = df_inner.index,
                            columns = ['运行内存/GB','存储容量/GB'])
df_inner = pd.merge(df_inner,df_split,right_index= True,left_index=True)
print(df_inner)
df_inner ['价格档次'] = np.where(df_inner['价格/元']>6000,'高档','中档')
df_inner.loc[(df_inner['国家']=='China')& (df_inner['屏幕尺寸']>6.2),'国产大屏']='YES'

df_inner['综合性能'] = df_inner['屏幕尺寸'].astype('float32')* 100 +\
                     df_inner['运行内存/GB'].astype('int') * 25 +\
                     df_inner['存储容量/GB'].astype('int')
df_inner['性价比'] = np.where(df_inner['综合性能']/df_inner['价格/元']>0.18,'高','一般')

df_inner.to_excel('手机统计数据.xlsx',sheet_name='mobile_sheet')
df_inner.to_csv('手机统计数据.csv')
