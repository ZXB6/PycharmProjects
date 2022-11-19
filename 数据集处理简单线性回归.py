from collections import OrderedDict
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression


examDict={'学习时间':[0.5,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50],
         '分数':[10,22,13,43,20,22,33,50,62,48,55,75,62,73,81,76,64,82,90,93]}
examOrderDict=OrderedDict(examDict)
examDf=pd.DataFrame(examOrderDict)
examDf.head()
# 提取特征features
exam_X=examDf.loc[:, '学习时间']
# 提取标签label
exam_y=examDf.loc[:, '分数']

# 散点图matplotlib
plt.scatter(exam_X,exam_y,color="b",label="exam data")
# 添加图标
plt.xlabel("Hours")
plt.ylabel("Score")
# 显示图像
plt.show()


X_train,X_test,y_train,y_test = train_test_split(exam_X,exam_y,train_size= .8)
#输出特征和标签
print('原始数据特征：',exam_X.shape,
     '训练集数据特征：',X_train.shape,
     '测试集数据特征：',X_test.shape)
print('原始数据标签：',exam_X.shape,
     '训练集数据标签：',y_train.shape,
     '测试集数据标签：',y_test.shape)

# 相关系数矩阵
rDf = examDf.corr()
rDf
# 将训练集特征转化为二维数组**行1列
X_train = np.array(X_train).reshape(-1,1)
# 将测试集特征转化为二维数组**行1列
X_test = np.array(X_test).reshape(-1,1)

# 创建模型
model = LinearRegression()
model.fit(X_train, y_train)
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

# 最佳拟合线
a = model.intercept_
b = model.coef_
print('最佳拟合线：截距为', a, ',回归系数为', b)
model.score(X_test, y_test)

