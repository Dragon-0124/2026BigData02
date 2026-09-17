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

df2.loc[df2['Review'] == "Superb 9.0", "Review"] = "Superb" # Review 열의 Review 값이 "Superb 9.0"인 행의 Review 값을 "Superb"로 변경
df2.loc[df2['Review'] == "Exceptional 10", "Review"] = "Exceptional" # Review 열의 Review 값이 "Exceptional 10"인 행의 Review 값을 "Exceptional"로 변경   


# print(df2.loc[df2['Review'] == "Review score ", ["Review"]]) # Review 열의 Review 값이 "Review score "인 행의 Review 값을 출력
# print(df2.loc[df2['Review'] == "Review score ", ["Review", "Rating"]])
# print(df2.loc[df2['Review'] == "Good", ["Review", "Rating"]])

df2.loc[df2['Review'] == "Review score ", "Review"] = "Good"

print(df2['Review'].value_counts())