import pandas as pd

df = pd.read_csv('datasets/APPL_price/APPL_price.csv')
# print(df.head())
# print(df.tail())
# print(df.info())



df['Date'] = pd.to_datetime(df['Date']) # str -> datetime 변환
# print(df.info())

df = df.set_index('Date') # Date 컬럼을 index로 설정
print(df.head())

# print(df['1990-11-02':'1990-11-10'])
print(df['2015-02':'2015-02'])
