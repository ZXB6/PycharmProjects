import pandas as pd
import numpy as np
income=pd.read_excel(r'income.xlsx')
# 数据的探索性分析
income.describe()         #数值型变量的统计描述
income.describe(include =['object'])       #离散型变量的统计描述
# 离散变量的重编码
for feature in income.columns:
    if income[feature].dtype == 'object':
        income[feature] = pd.Categorical(income[feature]).codes
income.head()
print(income)