import numpy as np
import pandas as pd

df2 = pd.read_csv('datasets\\bookings\\Bookings.csv')


# print(df2.info())
# print(df2['Review'])
# print(df2['Review'].value_counts())

#------------------------- 띄워쓰기 제거 -------------------------#

df2.loc[df2['Review'] == "Good ", "Review"] = "Good" 
df2.loc[df2['Review'] == "Very good ", "Review"] = "Very good" 
df2.loc[df2['Review'] == "Superb ", "Review"] = "Superb" 
df2.loc[df2['Review'] == "Fabulous ", "Review"] = "Fabulous" 
df2.loc[df2['Review'] == "Exceptional ", "Review"] = "Exceptional"

#----------------------------------------------------------------#

df2.loc[df2['Review'] == "Superb 9.0", "Review"] = "Superb"
df2.loc[df2['Review'] == "Exceptional 10", "Review"] = "Exceptional"
df2.loc[df2['Review'] == "Review score ", "Review"] = "Good"

# print(type(df2['Total_Review'].unique()))
# print(df2['Total_Review'].unique())
# print(df2['Total_Review'].value_counts())

df2['Total_Review'] = df2['Total_Review'].map(lambda x: str(x).replace('external','').strip()) # map() : 시리즈의 각 요소에 함수를 적용, strip() : 문자열 양쪽 공백 제거
df2['Total_Review'] = df2['Total_Review'].map(lambda x: str(x).replace('review','').strip()) # replace('1','2') '1'을 '2'로 바꿔줌
df2['Total_Review'] = df2['Total_Review'].map(lambda x: str(x).replace(',','')) # ,같은 기호를 포함한 문자열이 포함되어 있으면 실수로 타입을 변환할 수 없음
df2['Total_Review'] = df2['Total_Review'].astype('float') # astype() : 데이터 타입을 바꿔줌

# print(df2['Total_Review'].value_counts())
# print(df2['Total_Review'].unique())
print(df2['Total_Review'].describe())