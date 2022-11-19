import pandas as pd
import numpy as np
data=pd.read_csv(r'heart.csv')
cp=pd.get_dummies(data['cp'])
cp.columns=['cp'+str(i)for i in cp.columns]
ca=pd.get_dummies(data['ca'])
ca.columns=['ca'+str(i)for i in ca.columns]
thal=pd.get_dummies(data['thal'])
thal.columns=['thal'+str(i)for i in thal.columns]
data1=pd.concat([ca,cp,thal,data[['age','sex','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','target']]],axis=1)
print(data1)