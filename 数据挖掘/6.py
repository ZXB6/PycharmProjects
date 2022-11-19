import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='车次上车人数统计表.xlsx'
data=pd.read_excel(path)
tb=data.loc[data['车次'] == 'D02',['日期','上车人数']]
tb=tb.sort_values('日期')
tb1=data.loc[data['车次'] == 'D03',['日期','上车人数']]
tb1=tb1.sort_values('日期')
y1=tb.iloc[:,1]
y2=tb1.iloc[:,1]
plt.figure(5)
plt.boxplot([y1.values,y2.values])
plt.xticks([1,2], ['D02','D03'], rotation = 0)
plt.title('D02、D03车次上车人数箱线图')
plt.ylabel('上车人数')
plt.xlabel('车次')
plt.show()
