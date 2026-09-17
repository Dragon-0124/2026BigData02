import numpy as np
import pandas as pd

df1 = pd.read_csv('Project\\week03\\bike.csv')

# df1 = df1.rename({'registered': 'registered_user', 'casual': 'casual_user'}, axis=1)
df1.rename({'registered': 'registered_user', 'casual': 'casual_user'}, axis=1, inplace=True) # inplace=True를 사용하여 원본 DataFrame을 수정

# print(df1.head())
# print(df1.info())

# print(df1.describe(include='str'))  # 문자열 데이터를 포함한 통계 요약 정보 출력
# print(df1.describe(include='float'))  # 실수형 데이터를 포함한 통계 요약 정보 출력
print(df1.describe(exclude='int'))  # 정수형 데이터를 제외한 통계 요약 정보 출력