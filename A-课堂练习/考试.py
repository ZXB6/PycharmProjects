import pandas as pd

excel =pd.read_excel('score.xlsx',sheet_name=[0,1],header=0)
score =pd.DataFrame(excel[0])
duty = pd.DataFrame(excel[1])
print(score[0:3])
print('行数:'+str(score.shape[0]))

score['总分'] = score['数学'] + score['英语'] + score['语文']
score.sort_values(by='总分', inplace=True, ascending=False)  # 依据“总分”列的值从高到低进行排序
print('男生的平均分:'+str(score.groupby(['性别'])['总分'].mean()[0]))
print('女生的平均分:'+str(score.groupby(['性别'])['总分'].mean()[1]))
print('男生的最高分:'+str(score.groupby(['性别'])['总分'].max()[0]))
print('女生的最高分:'+str(score.groupby(['性别'])['总分'].max()[1]))

score.loc[(score['总分'] >= 270), '等级'] = 'A'
score.loc[(score['总分'] < 270) & (score['总分'] >= 210), '等级'] = 'B'
score.loc[(score['总分'] < 210), '等级'] = 'C'
Students = pd.merge(score, duty, how="left", on='学号')
Students.to_excel('students.xlsx')
