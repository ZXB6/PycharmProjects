import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.DataFrame(pd.read_csv('2018世界杯球队数据.csv',encoding = 'gbk'))

print("2.净胜球大于0的队伍：")
print(df.球队[df.进球> df.失球])

print("3.被罚红牌的队伍：")
print(df.球队[df.红牌==1])

print("4.进球率大于10%的队伍：")
df1 = df[['球队','进球','射门']]
print(df1[(df.进球 / df.射门) > 0.1])

print("5.进球数超过平均数且被罚黄牌少于5张的球队伍：")
df2 = df[['球队','进球','黄牌']]
print(df2[(df.进球 > df.进球.mean()) & (df.黄牌<5)] )

print("6.按照进球数降序输出所有球队及进球信息：")
df3 = df[['球队','进球']]
print(df3.sort_values(by='进球',ascending=False))

print("7.按照所属区进行分组，按升序统计输出每个区的进球数：")
df4 = df.groupby(df['所属区']).sum()
df5 = df4[['进球']]
print(df5.sort_values(by = '进球'))

# 8 题
plt.rcParams['font.sans-serif']=['SimHei']
df5.plot(kind='bar',title='所属区及进球数')
plt.show()

# 9 题
df6=df[['球队','黄牌']]
df6.plot(kind='bar',title='球队序号及黄牌数')
df3.plot(kind='bar',title='球队序号及进球数')
plt.show()