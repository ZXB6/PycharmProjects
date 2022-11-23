import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  scipy.stats import chi2_contingency as chi
data = pd.read_excel(r'个人信息数据采集表2022年.xlsx')
del data['序号']
#data.apply(lambda x:0 if x.isnull() else x)
data.apply(lambda x:np.sum(x.isnull()))
data.fillna({'大英1':data['大英1'].mean()},inplace=True)
data['视听说1'] = data['视听说1'].apply(lambda x : str(x).replace('，', '') if '，' in str(x) else x).astype(float)
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
#print(data)

#分析数学成绩好的同学是否计算机课程成绩也好？
data['高考数学成绩'] = data['高考数学成绩'].apply(lambda x:x*2/3)
plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False
plt.scatter( (data['高考数学成绩'] + data['高数1、2平均成绩']) / 2, (data['C语言成绩'] + data['数据结构成绩']) / 2)
plt.title('数学成绩与计算机成绩散点图')
plt.ylabel('计算机成绩')
plt.xlabel('数学成绩')
#plt.show()

#城市生源学生是否更可能过英语四级？
data['是否通过四级'] = data['通过四级时间'].apply(lambda x: "未通过" if x == "努力中" or x == "努力种" else "已通过")
#print(data['是否通过四级'])
## 卡方检验
print(pd.crosstab(data['是否通过四级'], data['城市or农村'], margins=True))
kf = chi(np.array([[56, 37], [17, 14]]))
#print('chisq-statistic=%.4f,  p-value=%.4f,   df=%i  expected_frep=%s'%kf)

#四级通过与大学英语成绩相关
# 取大英1至视听说4的平均成绩作为大学英语成绩
data['大学英语成绩'] = (data['大英1']+data['视听说1']+data['大英2']+data['视听说2']+data['大英3']+data['视听说3']+data['大英4']+data['视听说4'])/8
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
df = pd.DataFrame({'大学英语成绩': data["大学英语成绩"], '四级通过':data["是否通过四级"]})
anovat = anova_lm(ols('大学英语成绩 ~四级通过', data=df).fit(),type=2)
#print(anovat)


#打游戏的跟性别有关系吗
def timearray(s):
    if s == '0': return 0
    elif s == '0-1h': return 0.5
    elif s == '0~1h': return 0.5
    elif s == '1-4h': return 2.5
    elif s == '1-7h': return 4
    elif s == '100h+': return 100
    elif s == '10h': return 10
    elif s == '12h': return 12
    elif s == '14-21h': return 18
    elif s == '14h-21h': return 18
    elif s == '15h': return 15
    elif s == '1h': return 1
    elif s == '1h以内': return 1
    elif s == '1到10h': return 5.5
    elif s == '1－7h': return 4
    elif s == '20h': return 20
    elif s == '21h以上': return 21
    elif s == '24+': return 24
    elif s == '25h': return 25
    elif s == '3-4h': return 3.5
    elif s == '36h': return 36
    elif s == '4h': return 4
    elif s == '5h': return 5
    elif s == '7-14h': return 10.5
    elif s == '7h以上': return 8
    elif s == '8': return 8
    elif s == 'nan': return np.NaN
data['每周游戏时间'] = data['每周游戏时间'].astype(str)
data['每周游戏时间'] = data['每周游戏时间'].apply(timearray)
data['性别'] = data['性别'].apply(lambda x: 1 if x == '男' else 0)
df2 = pd.DataFrame(data)
anovat = anova_lm(ols('每周游戏时间~性别 ', data=df2).fit())
#print(anovat)


#高考成绩与四级通过有关吗
data['高考成绩']=data['高考数学成绩']+data['高考英语成绩']
df3=pd.DataFrame({'四级通过':data["是否通过四级"], '高考成绩': data["高考成绩"]})
anovat = anova_lm(ols('高考成绩~四级通过', data=df3).fit())
#print(anovat)

#晨读是否有助于提高英语视听说成绩
data['是否有早读习惯']=data['是否有早读习惯'].apply(lambda x: 1 if x == "是" else 0)
data['英语视听说成绩']=(data['视听说1']+data['视听说2']+data['视听说3']+data['视听说4'])/4
df4=pd.DataFrame({'是否有早读习惯':data["是否有早读习惯"], '英语视听说成绩': data["英语视听说成绩"]})
anovat = anova_lm(ols('英语视听说成绩~是否有早读习惯', data=df4).fit())
#print(anovat)


from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
item_list = []
for ind in data.index:
    list=[]
    for i in (data.loc[ind]['种类1'],data.loc[ind]['种类2'],data.loc[ind]['种类3']):
        if type(i)==str:
            list.append(i)
    item_list.append(list)

dic = {"娱乐": "娱乐消遣类","文学": "文学类读物",
       "科普": "科普读物","技术": "应用技术类",
       "应用": "应用技术类","经典":"经典名著",
       "名著":"经典名著","小说": "小说类"}
for item in item_list:
    for i, v in enumerate(item):
        for key in dic.keys():
            if key in v:
                item[i] = dic[key]
                break
for i in range(len(item_list)):
    item_list[i] = sorted(item_list[i])


te = TransactionEncoder()
tf = te.fit_transform(item_list)
df5 = pd.DataFrame(tf,columns=te.columns_)

# use_colnames=True表示使用元素名字，默认的False使用列名代表元素, 设置最小支持度min_support
frequent_itemsets = apriori(df5, min_support=0.05, use_colnames=True)
frequent_itemsets.sort_values(by='support', ascending=False, inplace=True)
print(frequent_itemsets[frequent_itemsets.itemsets.apply(lambda x: len(x)) == 2])


association_rule = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.1)
association_rule.sort_values(by='confidence', ascending=False, inplace=True)

df6=data.loc[:,["是否有早读习惯","大学期间是否谈恋爱"]]
df6['是否有早读习惯'] = data['是否有早读习惯'].apply(lambda x:False if x == 0 else True)
df6['大学期间是否谈恋爱'] = data['大学期间是否谈恋爱'].apply(lambda x:False if x == '否' else True)

# use_colnames=True表示使用元素名字，默认的False使用列名代表元素, 设置最小支持度min_support
frequent_itemsets = apriori(pd.concat([df5,df6],axis=1), min_support=0.05, use_colnames=True)
frequent_itemsets.sort_values(by='support', ascending=False, inplace=True)
print(frequent_itemsets[frequent_itemsets.itemsets.apply(lambda x: len(x)) == 2])

df7=data.loc[:,["是否有早读习惯","是否通过四级"]]
df7['是否有早读习惯'] = data['是否有早读习惯'].apply(lambda x:False if x == 0 else True)
df7['是否通过四级']  =data['通过四级时间'].apply(lambda x:False if x=="未通过" else True)
#print(df7)
frequent_itemsets = apriori(pd.concat([df6,df7],axis=1), min_support=0.05, use_colnames=True)
frequent_itemsets.sort_values(by='support', ascending=False, inplace=True)
print(frequent_itemsets[frequent_itemsets.itemsets.apply(lambda x: len(x)) == 2])
