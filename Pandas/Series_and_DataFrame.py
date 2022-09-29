# pandas의 Series와 DataFrame 정의하기
import pandas as pd
import numpy as np

# Series 정의하기
obj = pd.Series([4, 7, -1, 2])
"""
0   4
1   7
2   -1
3   2
dtype: int64 -> 데이터의 타입 (64비트 int형 자료)
"""

# Series의 값만 확인하기
print(obj.values)
"""
[ 4  7 -1  2]
"""

# Series의 index 확인하기
print(obj.index)
"""
RangeIndex(start=0, stop=4, step=1)
"""

# index 변경하기
obj.index = [5, 6, 7, 8]

# Series 초기화 시 index 설정
obj2 = pd.Series([4, 7, -1, 2], index=['a', 'b', 'c', 'd'])

# dictionary 자료형을 Series로 만들 수 있다
# key값이 Series의 index가 된다
dict_data = {'a': 4, 'b': 7, 'c': -1, 'd': 2}
dict_set = pd.Series(dict_data)

########################################################################################################################
# DataFrame 정의하기
# dictionary 또는 numpy의 array로 정의 할 수 있다
data = {'name': ['Kim', 'Lee', 'Song', 'Hwang'],
        'grade': [1, 4, 3, 2],
        'id': [20, 18, 17, 19]}

df = pd.DataFrame(data)
print(df)
"""
    name    grade   id
0    Kim        1   20
1    Lee        4   18
2   Song        3   17
3  Hwang        2   19
"""

# 세로 인덱스 (행 방향의 index)
print(df.index)
"""
RangeIndex(start=0, stop=4, step=1)
"""

# 가로 인덱스 (열 방향의 index)
print(df.columns)
"""
Index(['name', 'grade', 'id'], dtype='object')
"""

# DataFrame의 값 얻기
print(df.values)
"""
array([['Kim', 1, 20],
       ['Lee', 4, 18],
       ['Song', 3, 17],
       ['Hwang', 2, 19]], dtype=object) -> numpy array로 반환
"""

# 각 index의 이름 설정하기
df.index.name = 'Num'
df.columns.name = 'Info'

# DataFrame 초기화 시 index, columns 설정하기
# columns의 순서를 변경 할 수 있다
df2 = pd.DataFrame(data, columns=['id', 'grade', 'name'], index=['one', 'two', 'three', 'four'],)

# describe 함수는 DataFrame에서 계산 가능한 다양한 값들을 보여준다
print(df.describe())
