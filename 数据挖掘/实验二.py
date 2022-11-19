import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_excel(r'个人信息数据采集表2022年.xlsx')
del data['序号']
data.apply(lambda x:np.sum(x.isnull()))
def f(s):
    s = str(s)
    if '，' in s:
        s = s.replace('，', '')
    return s
data.fillna({'大英1':data['大英1'].mean()},inplace=True)
data['视听说1'] = data['视听说1'].apply(f).astype(float)
data.fillna({'视听说1':data['视听说1'].mean()},inplace=True)
data.fillna({'大英2':data['大英2'].mean()},inplace=True)
data.fillna({'视听说2':data['视听说2'].mean()},inplace=True)
data.fillna({'大英3':data['大英3'].mean()},inplace=True)
data.fillna({'大英4':data['大英4'].mean()},inplace=True)
data.fillna({'视听说3':data['视听说3'].mean()},inplace=True)
data.fillna({'视听说4':data['视听说4'].mean()},inplace=True)
data.fillna({'高考英语成绩':data['高考英语成绩'].mean()},inplace=True)
data.fillna({'第一次参加四级考试成绩':data['第一次参加四级考试成绩'].mean()},inplace=True)
data.fillna({'高数1、2平均成绩':data['高数1、2平均成绩'].mean()},inplace=True)
data.fillna({'高考数学成绩':data['高考数学成绩'].mean()},inplace=True)
data.fillna({'C语言成绩':data['C语言成绩'].mean()},inplace=True)
data.fillna({'数据结构成绩':data['数据结构成绩'].mean()},inplace=True)
#print(data['每周游戏时间'].astype(str))
print(data)
#分析数学成绩好的同学是否计算机课程成绩也好？
data['高考数学成绩'] = data['高考数学成绩'].apply(lambda x:x*2/3)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter( (data['高考数学成绩'] + data['高数1、2平均成绩']) / 2, (data['C语言成绩'] + data['数据结构成绩']) / 2)
plt.title('数学成绩与计算机成绩散点图')
plt.ylabel('计算机成绩', size=12)
plt.xlabel('数学成绩', size=12)
plt.show()