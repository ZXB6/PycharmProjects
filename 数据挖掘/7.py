import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
Titanic = pd.read_csv(r'titanic_train.csv')
Age_Male = Titanic.Age[Titanic.sex =='male']
# 取出女性年龄
Age_Female = Titanic.Age[Titanic.sex =='female']
# 绘制男乘客年龄的直方图
sns.displot(Age_Male, bins=20, kde=False, label ='男性')
# 绘制女乘客年龄的直方图
sns.displot(Age_Female, bins=20, kde=False, label ='女性')
plt.title('男女乘客的年龄直方图')
plt.legend()  # 显示图例
plt.show()  # 显示图形
# 绘制男女乘客年龄核密度图
sns.displot(Age_Male, hist=False, kde_kws={'color':'red', 'linestyle':'-'}, norm_hist = True, label ='男性')
sns.displot(Age_Female, hist=False, kde_kws={'color':'black', 'linestyle':'--'}, norm_hist = True, label ='女性')
plt.title('男女乘客的年龄核密度图')
plt.legend()  # 显示图例
plt.show()  # 显示图形
