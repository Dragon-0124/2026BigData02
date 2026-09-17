import numpy as np
import pandas as pd

df2 = pd.read_csv('datasets\\bookings\\Bookings.csv')


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

# print(df2['Rating'].isna())
# print(df2[df2['Rating'].isna()].head(5))
# print(df2[df2['Rating'].isna()].head(5).index)

index= df2[df2['Rating'].isna()].head(5).index
# print(index)

df2["Rating"] = df2["Rating"].fillna(df2["Rating"].median()) # mean도 가능

# print(df2.info())
# print(df2["Rating"].head())
# print(df2.iloc[167:172, 1:4])
print(df2.loc[index, "Review":"Rating"])