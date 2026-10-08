import seaborn as sb
import numpy as np
import pandas as pd

df = sb.load_dataset('titanic')

# print(df.head())
# print(df.groupby('sex')['survived'].mean())
# print(df.groupby(['sex','class'])['survived'].mean())
# print(df.groupby(['sex','class'])['survived'].agg(['count','mean', 'median']))
# print(df.groupby(['sex','class'])[['survived', 'age']].agg({'survived': 'median', 'age': 'max'}))

def get_IQR(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    return (np.abs(Q3 - Q1) * 1.5)
# 이상치를 판별하기 위해서 50%만 하면 이상치가 너무 많이 잡힐 수 있으니 1.5를 곱해서 이상치를 판별한다. 
# 정상적인 IQR의 범위는 Q3 - Q1 (50%) 이다.

print(df.groupby(['sex','class'])['age'].apply(get_IQR))