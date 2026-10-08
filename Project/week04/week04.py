import seaborn as sns
import pandas as pd

'''
df1 = pd.DataFrame(
    {'group':['A','A','A','B','B'],
    'value':[1, 1, 1, 10, 10]}
)
print(df1)
'''

df = pd.DataFrame(
    [['A', 1], ['A', 1], ['A', 1], ['B', 10], ['B', 10]], columns=['group', 'value']
)
# print(df)

print(df.groupby([1,0,1,0,1])['value'].mean()) # 0, 1끼리 그룹화


s = pd.Series([True, False, True, False, True])
print(df.groupby(s)['value'].mean())