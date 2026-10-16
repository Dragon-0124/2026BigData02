import pandas as pd

df = pd.read_csv('datasets\\German_credit\\German_credit.csv')

# print(df.info())
# print(df.tail())

# print(pd.cut((df['Age']), bins=8)) # 나이를 8구간으로 나누기

ages = [10, 20, 30, 40, 50, 60, 70, 80]
# print(pd.cut((df['Age']), ages, right=True)) # 초과 - 이하 기본값이라 True옵션은 주로 생략함
print(pd.cut((df['Age']), ages, right=False)) # right=False 옵션을 주면 이상 - 미만으로 바뀐다


# print(pd.cut((df['Age']), bins=8).reset_index().groupby('Age').size())

