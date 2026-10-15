import pandas as pd

df = pd.read_csv('datasets/APPL_price/APPL_price.csv')
df['Date'] = pd.to_datetime(df['Date']) # str -> datetime 변환
df = df.set_index('Date') # Date 컬럼을 index로 설정

# print(df.resample('7D').mean())
print(df.resample('2ME').mean()) # 두 달 단위로 묶고, 각 묶음의 평균을 출력