import pandas as pd
#from sklearn.metrics import classfication_report
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
#加载sklearn库自带的经典数据集鸢尾花
iris=load_iris()
irisdf=pd.DataFrame(iris.data,columns=iris.feature_names)
irisdf.head(5)      #查看前5个实例的属性
#第二步：分割训练集和测试集
irris_data=iris[‘data’]   #取出数据集中的数据(即特征)
irris_target=irris[‘target’]     #取出数据集中的类别标签
irris_names=irris[‘feature_names’]  #取出数据集的特征名
Xtrain, Xtest, Ytrain, Ytest = train_test_split(irris_data,irris_target,test_size=0.2)
#第三步：建立模型
dct=DecisionTreeClassifier()  #初始化
dct.fit(Xtrain,Ytrain)  # 拟合
y_pred = dct.predict(Xtest)# 输入测试数据送到训练好的模型里，输出预测的类
print(dct.score(Xtest,Ytest))#查看模型(测试集)的准确度
#或查看各个类别精确度、召回率和F1分数等信息
#print(classification_report(irris_target,dct.predit(irris_data)))
