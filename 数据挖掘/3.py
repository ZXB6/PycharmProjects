import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path='车次上车人数统计表.xlsx';
data=pd.read_excel(path);
tb=data.loc[data['车次'] == 'D02',['日期','上车人数']].sort_values('日期');
x=np.arange(1,len(tb.iloc[:,0])+1)
y1=tb.iloc[:,1]
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.scatter(x,y1)
plt.xlabel('日期')
plt.ylabel('上车人数')
plt.xticks([1,5,10,15,20,24], tb['日期'].values[[0,4,9,14,19,23]], rotation = 90)
plt.title('D02车次上车人数散点图')
plt.show()