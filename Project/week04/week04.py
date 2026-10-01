import numpy as np
import pandas as pd

df1 = pd.read_csv('datasets\\bookings\\Bookings.csv')

#------------------------- 띄워쓰기 제거 & 비슷한 데이터 통합-------------------------#

df1.loc[df1['Review'] == "Good ", "Review"] = "Good" 
df1.loc[df1['Review'] == "Very good ", "Review"] = "Very good" 
df1.loc[df1['Review'] == "Superb ", "Review"] = "Superb" 
df1.loc[df1['Review'] == "Fabulous ", "Review"] = "Fabulous" 
df1.loc[df1['Review'] == "Exceptional ", "Review"] = "Exceptional"
df1.loc[df1['Review'] == "Superb 9.0", "Review"] = "Superb"
df1.loc[df1['Review'] == "Exceptional 10", "Review"] = "Exceptional"
df1.loc[df1['Review'] == "Review score ", "Review"] = "Good"

#--------------------------------------------------------------------------------#

print(df1['Total_Review'].unique()) # before

# map() : 시리즈의 각 요소에 함수를 적용, strip() : 문자열 양쪽 공백 제거 / STRIP() : 문자열 양쪽 공백 제거
df1['Total_Review'] = df1['Total_Review'].map(lambda x: str(x).replace('external','').strip()) 
df1['Total_Review'] = df1['Total_Review'].map(lambda x: str(x).replace('review','').strip()) # replace('1','2') '1'을 '2'로 바꿔줌
df1['Total_Review'] = df1['Total_Review'].map(lambda x: str(x).replace(',','')) # ,같은 기호를 포함한 문자열이 포함되어 있으면 실수로 타입을 변환할 수 없음

print(df1['Total_Review'].unique()) #after

df1['Total_Review'] = df1['Total_Review'].astype('float') # astype() : 데이터 타입을 바꿔줌

print(df1.describe())

quantile = [0, 0.2, 0.4, 0.6, 0.8, 1]

for idx in quantile:
    # q = df1['Total_Review'].quantile(idx, interpolation='nearest') # interpolation='nearest' - 가장 가까운 값으로 보간
    # q = df1['Total_Review'].quantile(idx, interpolation='lower') # interpolation='lower' - 하위 값으로 보간
    q = df1['Total_Review'].quantile(idx, interpolation='higher') # interpolation='higher' - 상위 값으로 보간
    print(f'quantile({idx}) is {q}')
    