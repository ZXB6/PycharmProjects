import numpy as np
import pandas as pd
scores = np.random.uniform(0,100,size=30)  # 我们先给 scores传入30个从0到100随机的数
scores = np.round(scores,1)                           # 然后使用 np.round()函数控制数据精度
# 指定箱子的分界点
bins = [0,59,70,85,100]
cuts = pd.cut(scores,bins)
#默认情况下，cut()的区间划分是左开右闭，可以传递right=False来改变哪一边是封闭的
#cuts = pd.cut(scores,grades,right=False)
#也可以通过向labels选项传递一个列表或数组来传入自定义的箱名
group_names = ['不及格','及格','良','优秀']
cuts = pd.cut(scores,bins,labels=group_names)
print('scores:',scores)
print('\ncuts:')
print(cuts)
# 我们还可以计算出每个箱子中有多少个数据
print('cats.value_counts:',pd.value_counts(cuts))