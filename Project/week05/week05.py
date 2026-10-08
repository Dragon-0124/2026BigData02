import seaborn as sb
import numpy as np
import pandas as pd


df = sb.load_dataset('titanic')

# print(df.head())
# print(df.groupby('sex')['survived'].mean())
# print(df.groupby(['sex','class'])['survived'].mean())
# print(df.groupby(['sex','class'])['survived'].agg(['count','mean', 'median']))
# print(df.groupby(['sex','class'])[['survived', 'age']].agg({'survived': 'median', 'age': 'max'}))
'''
def get_IQR(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
   return (np.abs(Q3 - Q1) * 1.5)
# 이상치를 판별하기 위해서 50%만 하면 이상치가 너무 많이 잡힐 수 있으니 1.5를 곱해서 이상치를 판별한다. 
# 정상적인 IQR의 범위는 Q3 - Q1 (50%) 이다.
print(df.groupby(['sex','class'])['age'].apply(get_IQR))
'''

df2 =  sb.load_dataset('penguins')
# print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean())
# print(df2.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean())))


# 특정 칼럼에서 결측치가 있는 행 선택
'''
print(df2.query('sex.isna()'))
print(df2[df2['sex'].isna()])
print(df2.loc[df2['sex'].isna()])
'''

# 전체 칼럼에서 결측치가 있는 행 선택
'''
# 결측치 개수가 1개 이상인 행 선택
df2[df2.isna().sum(axis=1) > 0]
# 결측치가 없는 행을 찾은 뒤 반전(~)해서 선택
df2[~df2.notna().all(axis=1)]
'''

print(df2[df2.isnull().any(axis=1)]) # 결측치가 있는 행만 출력
