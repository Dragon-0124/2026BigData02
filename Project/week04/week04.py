import seaborn as sns
import pandas as pd

pg = sns.load_dataset('penguins')

# print(pg.head())
# print(pg.describe())

# print(pg.query('bill_length_mm < 35'))
# print(pg[pg['bill_length_mm'] < 35])
# print(pg.loc[pg['bill_length_mm'] < 30])

# print(pg.query('bill_length_mm > 54 and species == "Chinstrap"'))


# bln = float(input("Enter the minimum bill length: "))
# species = input("Enter the species(Gentoo, Adelie, Chinstrap): ")
# print(pg.query('bill_length_mm >= @bln and species == @species'))


# query 메서드 조건문의 문자열 메서드 사용
# print(pg.query('island.str.contains("sc")'))
# print(pg.query('species.str.endswith("e")'))
# print(pg.query('species.str.startswith("Gen")'))

# isin을 이용한 리스트 내 항목 참조
filtering = ["Adelie", "Chinstrap"]
print(pg.query('species.isin(@filtering)'))