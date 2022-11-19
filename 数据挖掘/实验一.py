import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.DataFrame(pd.read_excel('香水.xlsx'))
plt.rcParams['font.sans-serif'] = 'SimHei'
# 第一问
data["评价"]=data["评价"].str.replace("+","")
l=[]
for column in data["评价"]:
        if str(column).endswith("万"):
            column=column.replace("万", "")
            column=int(float(column)*10000)
        l.append(int(column))
        #data["新评价"]=data.apply(column,axis=0)
data["评价"]=pd.DataFrame(l)
print(data["评价"])


# 第二问
# data2=data.适用场所.str.split("，",8,True)
data2=list()
for column in data['适用场所']:
    data2=list(set(data2+list(str(column).split("，"))))
data2.remove('nan')
for i in data2:
    data[i] = 0
i=0
for column2 in data['适用场所']:
    for x in list(str(column2).split("，")):
        if x!='nan':
            data[x][i]=1
    i+=1
print(data.iloc[:,11:])

# 第三问
data['商品产地']=data['商品产地'].replace(['中国大陆','广州','广东','中国大陆上海','中国广东','浙江义乌','浙江'],"中国")
print(data['商品产地'])

# 第四问
data["价格等级"]=pd.cut(data['价格'],bins=[-1,100,300,500,700,1000,999999],labels=["低","较低","中等","较高","高","非常高"])
print(data["价格等级"])
data["销量等级"]=pd.cut(data['评价'],bins=[-1,100,500,1000,2000,5000,10000,999999],labels=["非常低","低","较低","中等","较高","高","非常高"])
print(data["销量等级"])


#第5题各产地香水的销售分布
data5=list()
for column5 in data['商品产地']:
    data5 = list(set(data5 + list(str(column5).split(" "))))
data5.remove('nan')
data5.remove("")
#print(data5)
list5=[]
for i in data5:
    list5.append(data[data['商品产地']==i]['评价'])
#print(list5)
#绘制箱线图
plt.figure(1)
plt.boxplot(list5)
plt.xticks(range(1,len(data5)+1),data5,rotation=-25)
plt.title('箱图')
plt.ylabel('总销量')
plt.xlabel('产地')


#各包装香水销量
data5_2=list()
for column5_2 in data['包装']:
    data5_2 = list(set(data5_2 + list(str(column5_2).split(" "))))
    #print(data5_2)
data5_2.remove('nan')
#print(data5)
list5_2=[]
for i in data5_2:
    list5_2.append(data[data['包装']==i]['评价'])
#print(list5)
#绘制箱线图
plt.figure(2)
plt.boxplot(list5_2)
plt.xticks(range(1,len(data5_2)+1),data5_2)
plt.title('箱图')
plt.ylabel('总销量')
plt.xlabel('包装')


#不同香调的香水销售
data5_3=list()
for column5_3 in data['香调']:
    data5_3 = list(set(data5_3 + list(str(column5_3).split(" "))))
data5_3.remove('nan')
#print(data5)
list5_3=[]
for i in data5_3:
    list5_3.append(data[data['香调']==i]['评价'])
#print(list5)
#绘制箱线图
plt.figure(3)
plt.boxplot(list5_3)
plt.xticks(range(1,len(data5_3)+1),data5_3,rotation=-90)
plt.title('箱图')
plt.ylabel('总销量')
plt.xlabel('香调')

#不同净含量的香水销量
data5_4=list()
for column5_4 in data['净含量']:
    data5_4 = list(set(data5_4 + list(str(column5_4).split(" "))))
data5_4.remove('nan')
#print(data5)
list5_4=[]
for i in data5_4:
    list5_4.append(data[data['净含量']==i]['评价'])
#print(list5)
#绘制箱线图
plt.figure(4)
plt.boxplot(list5_4)
plt.xticks(range(1,len(data5_4)+1),data5_4,rotation=-25)
plt.title('箱图')
plt.ylabel('总销量')
plt.xlabel('净含量')
plt.show()
# 标签云
from wordcloud import WordCloud
from collections import Counter
arr=[]
arr1=["商品名称","价格","评价"]
for i in arr1:
    for j in data[i]:
        arr.append(str(j))
counts = Counter(arr)
wordcloud = WordCloud(font_path=r"C:\Windows\Fonts\simhei.ttf",max_font_size=40, relative_scaling=.5).fit_words(counts)
plt.figure(5)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

#气泡图
data7=list()
for column7 in data['商品名称']:
    data7 = list(set(data7 + list(str(column7).split(" "))))
data7.remove('')
list7=[]
for i in data7:
    if data[data['商品名称']==i]['评价'].sum()!=0:
        list7.append((data[data['商品名称']==i]["价格"].mean(),data[data['商品名称']==i]['评价'].replace(" ","").sum()))
list7=sorted(list7,key=lambda x:x[1])
list7_1=[]
list7_2=[]
for i in range(1,10):
     list7_1.append(list7[len(list7)-i][0])
     list7_2.append(list7[len(list7)-i][1])
#print(list7_1)
#print(list7_2)

plt.scatter(x=pd.DataFrame(list7_2),
            y=pd.DataFrame(list7_2)*7,
            s=pd.DataFrame(list7_1),
            color='steelblue',label='av')
plt.xlabel("评价数量")
plt.ylabel("销售数量")
plt.title("评价数量、销售数量及销售价格的气泡图")
plt.legend()
plt.show()


