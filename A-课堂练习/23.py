import pandas as pd

def grade(x):
    if x >= 270:
        return "A"
    elif x >= 210:
        return "B"
    else:
        return "C"

file_name = "score.xlsx"  # 定义文件路径，这里我是将代码和EXCEL放在了同一个文件夹下，如不在同一文件夹应写成C:/studata.xlsx形式
Score = pd.read_excel(file_name, sheet_name='Sheet1', index_col=0)  # 读取学生信息
Duty = pd.read_excel(file_name, sheet_name='Sheet2', index_col=0)  # 读取班级职务

Score['总分'] = Score['数学'] + Score['英语'] + Score['语文']
Score['等级'] = Score['总分'].apply(lambda x: grade(x))  # 新增一列“等级”
Score.sort_values(by='总分', inplace=True, ascending=False)  # 依据“总分”列的值从高到低进行排序

print('男女生的平均分为:')
print(Score.groupby(['性别'])['总分'].mean())  # 输出男女生各自的平均分
print('男女生的最高分为:')
print(Score.groupby(['性别'])['总分'].max())  # 输出男女生的最高分
Students = pd.merge(Score, Duty, on='学号')  # 以“学号”为关联关键,合并sheet1和sheet2
Students.to_excel('students.xlsx')

