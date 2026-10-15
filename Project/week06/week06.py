import pandas as pd

df = pd.read_csv('datasets\\Uber\\Uber.csv')

'''
print(df.head())
print(df.tail())
# print(df['MILES*'].sum()-12204.7) # Total MILES* 합계 - 12204.7
'''


df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce') # str -> datetime 변환
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')

# print(df['START*'].value_counts())
# print(df['STOP*'].value_counts())
# print(df['MILES*'].describe())

# print(df[df['MILES*'] == df['MILES*'].max()])

df1 = df.drop(1155) # 오류 행 제거

# print(df1[df1['MILES*'] == df1['MILES*'].max()])

# print(df1['PURPOSE*'].value_counts())

print(df1.isnull().sum()) # 결측치 확인

print(df1.info())


df1['DURATION*'] = (df1['END_DATE*'] - df1['START_DATE*']).dt.total_seconds() / 60 # DURATION(운행 시간) 컬럼 생성 후 분단위로 변환

print(df1.info())

print(df1.groupby(['CATEGORY*','PURPOSE*'])[['MILES*','DURATION*']].agg(['median','mean','count','std'])) # 목적별 평균 운행 시간