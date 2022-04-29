import pandas as pd
import numpy as np

# region 1、Series
'''
Series 由索引（index）和列组成
参数说明：
data：一组数据(ndarray 类型)。
index：数据索引标签，如果不指定，默认从 0 开始。
dtype：数据类型，默认会自己判断。
name：设置名称。
copy：拷贝数据，默认为 False。
'''
# 实例1：简单的 Series 实例
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar)
# 实例2：索引值就从 0 开始
a = [1, 2, 3]
myvar = pd.Series(a)
print(myvar[1])
# 实例3： 指定索引值
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
# 实例4：根据索引值读取数据
a = ["Google", "Runoob", "Wiki"]
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar["y"])
# 实例5：使用 key/value 对象，类似字典来创建 Series
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites)
print(myvar)
# 实例6：只需要字典中的一部分数据，只需要指定需要数据的索引即可
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites, index=[1, 2])
print(myvar)
# 实例7：设置 Series 名称参数
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}
myvar = pd.Series(sites, index=[1, 2], name="RUNOOB-Series-TEST")
print(myvar)
# endregion Series

#region 2、DataFrame
'''
参数说明：DataFrame 是一个二维的数组结构，类似二维数组
data：一组数据(ndarray、series, map, lists, dict 等类型)。
index：索引值，或者可以称为行标签。
columns：列标签，默认为 RangeIndex (0, 1, 2, …, n) 。
dtype：数据类型。
copy：拷贝数据，默认为 False。
'''
# 实例1：使用列表创建
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
df = pd.DataFrame(data, columns=['Site', 'Age'], dtype=float)
print(df)
# 实例2：使用 ndarrays 创建
data = {'Site': ['Google', 'Runoob', 'Wiki'], 'Age': [10, 12, 13]}
df = pd.DataFrame(data)
print(df)
# 实例3： 使用字典创建
data = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print(df)
# 实例4：可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 0，第二行索引为 1
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
# 实例5：返回多行数据，使用 [[ ... ]] 格式，... 为各行的索引，以逗号隔开
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行和第二行
print(df.loc[[0, 1]])
# 实例6：指定索引值
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)
# 实例7：可以使用 loc 属性返回指定索引对应到某一行
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])
#endregion
