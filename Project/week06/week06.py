import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress


df = pd.read_csv('datasets\\Uber\\Uber.csv')

df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce') # str -> datetime 변환
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')

df1 = df.drop(1155) # 오류 행 제거

df1['DURATION*'] = (df1['END_DATE*'] - df1['START_DATE*']).dt.total_seconds() / 60 # DURATION(운행 시간) 컬럼 생성 후 분단위로 변환

df1 = df1.dropna()

# s: slope, i: intercept, r: correlation, p: p-value, std_err: standard error, _: Non Used values
s, i, r, _, _ = linregress(df1['MILES*'], df1['DURATION*']) # X: MILES*, Y: DURATION*에 대한 선형회귀분석 수행
# print(s, i, r) # 기울기, 절편, 상관계수(1이면 강한 양의 상관관계, -1이면 강한 음의 상관관계) 출력



fig, ax = plt.subplots()
sns.regplot(x='MILES*', y='DURATION*', data=df1, ax=ax) # 회귀선과 산점도 시각화
# plt.legend()
plt.show()