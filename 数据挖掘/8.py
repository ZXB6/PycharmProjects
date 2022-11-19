# (1)绘制日期为2017年1月3日-2017年1月20日的收盘价格走势图
# (2)绘制日期为2017年1月3日-2017年1月20日的交易柱状图
# (3)计算日期为2017年1月-2017年11月的交易量，并绘制其饼图
# (4)将以上的价格走势图、柱状图、饼图在同一个figure上以子图的形式绘制出来
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('trd.xlsx')
dt = data.loc[data['股票代码'] == 600000, ['交易日期', '收盘价', '交易量']]
plt.rcParams['font.sans-serif'] = 'SimHei'

data1 = dt.iloc[ (dt['交易日期'].values >= '2017-01-03') & (dt['交易日期'].values <= '2017-01-20') , :]
y1 = data1['收盘价']
x1 = range(len(y1))
plt.figure(1)
plt.plot(x1, y1)
plt.xlabel('交易日期')
plt.ylabel('收盘价')
plt.title('收盘价格走势图')

data2 = dt.iloc[(dt['交易日期'].values >= '2017-01-03') & (dt['交易日期'].values <= '2017-01-20'), :]
y2 = data2['交易量']
x2 = range(len(y2))
plt.figure(2)
plt.bar(x2, y2)
plt.xlabel('交易日期')
plt.ylabel('交易量')
plt.title('交易柱状图')

Data = np.zeros((11))
for m in range(11):
    m = m + 1
    if m < 10:
        m1 = '2017-0' + str(m) + '-01'
        m2 = '2017-0' + str(m) + '-31'
    else:
        m1 = '2017-' + str(m) + '-01'
        m2 = '2017-' + str(m) + '-31'
    Data[m - 1] = dt.iloc[(dt['交易日期'].values >= m1) & (dt['交易日期'].values <= m2), [2]].sum()[0]
plt.figure(3)
plt.pie(Data, labels=range(1,12), autopct='%1.2f%%')
plt.title('月交易量饼图')

plt.figure(4)
plt.figure(figsize=(18, 6))
plt.subplot(1, 3, 1)
plt.plot(x1, y1)
plt.xlabel('交易日期')
plt.ylabel('收盘价')
plt.title('收盘价格走势图')
plt.subplot(1, 3, 2)
plt.bar(x2, y2)
plt.xlabel('交易日期')
plt.ylabel('交易量')
plt.title('交易柱状图')
plt.subplot(1, 3, 3)
plt.pie(Data, labels=range(1,12), autopct='%1.2f%%')
plt.title('月交易量饼图')
plt.show()
