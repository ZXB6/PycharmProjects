import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path='车次上车人数统计表.xlsx'
data=pd.read_excel(path)
D=data.iloc[:,0]
D=list(D.unique())
list1=[]
for d in D:
     dt=data.loc[data["车次"] == d,["上车人数"]]
     s=dt.sum()
     list1.append(s["上车人数"])
     plt.figure(4)
     plt.pie(list1, labels=D, autopct="% 1.2f %%")
     plt.title('各车次上车人数百分比饼图')
     plt.show()
