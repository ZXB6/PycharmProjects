import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
stuScore=np.loadtxt('score.csv',delimiter=',',skiprows=1)
sumEach=np.sum(stuScore[:,1:],axis=1)/2
avgEachCourse=np.average(stuScore[:, 1:],axis=0)

maxchinese=np.max(stuScore[:,1])
maxMath=np.max(stuScore[:,2])
maxEng=np.max(stuScore[:,3])
maxphy=np.max(stuScore[:,4])
maxchem=np.max(stuScore[:,5])
maxpolit=np.max(stuScore[:,6])
maxhis=np.max(stuScore[:,7])

minChinese=np.min(stuScore[:,1])
minMath=np.min(stuScore[:,2])
minEng=np.min(stuScore[:,3])
minphy=np.min(stuScore[:,4])
minchem=np.min(stuScore[:,5])
minpolit=np.min(stuScore[:,6])
minhis=np.min(stuScore[:,7])

print("每个学生的七门课程总分")
print(sumEach)
print("所有学生的每门课程平均分")
print(avgEachCourse)
print("每门课程最高分")
print(maxchinese,maxMath,maxEng,maxphy,maxchem,maxpolit,maxhis)
print("每门课程最低分")
print(minChinese,minMath,minEng,minphy,minchem,minpolit,minhis)

ChineseScore=stuScore[:,1]
mathScore=stuScore[:,2]
engScore=stuScore[:,3]
pyhScore=stuScore[:,4]
chemScore=stuScore[:,5]
politScore=stuScore[:,6]
hisScore=stuScore[:,7]
plt.suptitle("课程分布直方图")

plt.subplot(7,2,1)
plt.hist(mathScore,bins=10,range=(0,100),color='red')
plt.xlabel("高数成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()

plt.subplot(7,2,2)
plt.hist(engScore,bins=10,range=(0,100),color='green')
plt.xlabel("英语成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()

plt.subplot(7,2,5)
plt.hist(ChineseScore,bins=10,range=(0,100),color='red')
plt.xlabel("语文成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()

plt.subplot(7,2,6)
plt.hist(pyhScore,bins=10,range=(0,100),color='green')
plt.xlabel("物理成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()

plt.subplot(7,2,9)
plt.hist(chemScore,bins=10,range=(0,100),color='red')
plt.xlabel("化学成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()
plt.show()

plt.subplot(7,2,10)
plt.hist(politScore,bins=10,range=(0,100),color='green')
plt.xlabel("政治成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()

plt.subplot(7,2,11)
plt.hist(hisScore,bins=10,range=(0,100),color='red')
plt.xlabel("历史成绩分数段")
plt.ylabel("人数")
plt.xlim(0,100)
plt.xticks([0,10,20,30,40,50,60,70,80,90,100])
plt.yticks([0,4,8,12,16,20])
plt.grid()
plt.show()