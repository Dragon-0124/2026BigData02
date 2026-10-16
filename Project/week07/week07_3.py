import pandas as pd

df = pd.read_csv('datasets\\APPL_price\\APPL_price.csv')

s = df['Close'] > 175
# print(s.sum()) # 1980s ~ 2022s 중 종가가 175달러를 초과한 날들의 합계(22일)

sc = s.cumsum()

# 애플 종가기준 175달러를 넘긴 날짜 중 연속적으로 175달러 이상을 유지한 최장 기간(9일)
# print(s.mul(sc).diff().where(lambda n: n<0).ffill().add(sc, fill_value=0).max())

# print(df[s])

# print(s.groupby((~s).cumsum()).sum().max())