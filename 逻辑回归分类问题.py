from collections import OrderedDict
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt

examDict={'学习时间':[0.5,0.75,1.00,1.25,1.50,1.75,1.75,2.00,2.25,2.50,2.75,3.00,3.25,3.50,4.00,4.25,4.50,4.75,5.00,5.50],
         '通过考试':[10,22,13,43,20,22,33,50,62,48,55,75,62,73,81,76,64,82,90,93]
          }
examOrderDict=OrderedDict(examDict)
examDf=pd.DataFrame(examOrderDict)
examDf.head()
# 提取特征features
exam_X=examDf.loc[:, '学习时间']
# 提取标签label
exam_y=examDf.loc[:, '通过考试']

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
# 将训练集特征转化为二维数组**行1列
X_train = np.array(X_train).reshape(-1,1)
# 将测试集特征转化为二维数组**行1列
X_test = np.array(X_test).reshape(-1,1)
# 创建模型
model=LogisticRegression()
# 训练模型
model.fit(X_train,y_train)
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
intercept_scaling =1, max_iter=100, multi_class='ovr', n_jobs=1,
penalty ='l2', random_state=None, solver='liblinear', tol=0.0001,
verbose =0, warm_start=False)
model.score(X_test,y_test)
# 实施模型
model.predict_proba(3)
# 预测数据：使用模型的predict方法可以进行预测。这里我们输入学生的特征学习时间3小时，模型返回结果标签是1，表示预测该学生通过考试。
pred=model.predict([[3]])
print(pred)

a = model.intercept_
b = model.coef_
x = 3
z = a+b*x
pred_Y=1/(1+np.exp(-z))
print('预测的概率值:',pred_Y)