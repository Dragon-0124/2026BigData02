import pandas as pd

s = pd.Series([0,0,1,1,0,1,1,1,1,0])
# print(s)

sc = s.cumsum() # 누적합계 (cumulative sum) 계산
# print(sc)
# print(s.mul(sc))  # multiply

# print(s.mul(sc).diff()) # difference : 뒤의 원소 값에서 앞의 원소 값 빼기 계산

# print(s.mul(sc).diff().where(lambda n: n<0)) # where 조건문에 속하는 원소 값을 제외한 나머지 값은 NaN처리

# print(s.mul(sc).diff().where(lambda n: n<0).ffill()) # f(orward)fill: 결측값을 앞의 원소의 값으로 채우기
# print(s.mul(sc).diff().where(lambda n: n<0).bfill()) # b(ackward)fill: 결측값을 뒤의 원소의 값으로 채우기
# print(s.mul(sc).diff().where(lambda n: n<0).ffill().add(sc, fill_value=0)) # fill_value - 결측값을 x로 처리

print(s.mul(sc).diff().where(lambda n: n<0).ffill().add(sc, fill_value=0).max())