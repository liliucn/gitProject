import pandas as pd
import numpy as np
import datetime
# 文章引用：https://mp.weixin.qq.com/s/moLPWHjtLBQcYttgHpFtkA

###  1、如何使用列表和字典创建 Series
ser1 = pd.Series([1.5, 2.5, 3, 4.5, 5.0, 6])
print('********ser1********：\n ',ser1)

# 使用 name 参数创建 Series
ser2 = pd.Series(["India", "Canada", "Germany"], name="Countries")
print('********ser2********：\n ',ser2)

# 使用简写的列表创建 Series
ser3 = pd.Series(["A"]*4)
print('********ser3********：\n ',ser3)

# 使用字典创建 Series
ser4 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
print('********ser4********：\n ',ser4)


###  2如何使用 Numpy 函数创建 Series
ser1 = pd.Series(np.linspace(1, 10, 5))
print('********ser1********：\n ',ser1)

ser2 = pd.Series(np.random.normal(size=5))
print('********ser2********：\n ',ser2)

###  3如何获取 Series 的索引和值
ser1 = pd.Series({"India": "New Delhi",
                  "Japan": "Tokyo",
                  "UK": "London"})
print(ser1.values)
print(ser1.index)
print("\n")
ser2 = pd.Series(np.random.normal(size=5))
print(ser2.index)
print(ser2.values)

###  4如何在创建 Series 时指定索引
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
ser1 = pd.Series(values, index=code)
print('********ser1********：\n ',ser1)

###  5如何获取 Series 的大小和形状
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
ser1 = pd.Series(values, index=code)
print(len(ser1))
print(ser1.shape)
print(ser1.size)

###  6如何获取 Series 开始或末尾几行数据

#【head()】
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
ser1 = pd.Series(values, index=code)
print("-----Head()-----")
print(ser1.head())
print("\n\n-----Head(2)-----")
print(ser1.head(2))

#【tail()】
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
ser1 = pd.Series(values, index=code)
print("-----Tail()-----")
print(ser1.tail())
print("\n\n-----Tail(2)-----")
print(ser1.tail(2))

#【Take()】
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
ser1 = pd.Series(values, index=code)
print("-----Take()-----")
print(ser1.take([2, 4, 5]))

### 7使用切片获取 Series 子集
num = [000, 100, 200, 300, 400, 500, 600, 700, 800, 900]
idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
series = pd.Series(num, index=idx)
print("\n [2:2] \n")
print(series[2:4])

print("\n [1:6:2] \n")
print(series[1:6:2])

print("\n [:6] \n")
print(series[:6])

print("\n [4:] \n")
print(series[4:])

print("\n [:4:2] \n")
print(series[:4:2])

print("\n [4::2] \n")
print(series[4::2])

print("\n [::-1] \n")
print(series[::-1])

print("\n [:4:2] \n")
print(series[:4:2])

print("\n [4::2] \n")
print(series[4::2])

print("\n [::-1] \n")
print(series[::-1])

### 8如何创建 DataFrame
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})
print(employees)

###  9如何设置 DataFrame 的索引和列信息
employees = pd.DataFrame(
    data={'Name': ['John Doe', 'William Spark'],
          'Occupation': ['Chemist', 'Statistician'],
          'Date Of Join': ['2018-01-25', '2018-01-26'],
          'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])
print(employees)

### 10如何重命名 DataFrame 的列名称
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]})
employees.columns = ['EmpCode', 'EmpName', 'EmpOccupation', 'EmpDOJ', 'EmpAge']
print(employees)

### 11如何根据 Pandas 列中的值从 DataFrame 中选择或过滤行
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\nUse == operator\n")
print(employees.loc[employees['Age'] == 23])

print("\nUse < operator\n")
print(employees.loc[employees['Age'] < 30])

print("\nUse != operator\n")
print(employees.loc[employees['Occupation'] != 'Statistician'])

print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] != 'Statistician') &  (employees['Name'] == 'John')])

### 12在 DataFrame 中使用“isin”过滤多行
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician','Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26','2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\nUse isin operator\n")
print(employees.loc[employees['Occupation'].isin(['Chemist', 'Programmer'])])

print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] == 'Chemist') | (employees['Name'] == 'John') & (employees['Age'] < 30)])

### 13迭代 DataFrame 的行和列
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\n Example iterrows \n")
for index, col in employees.iterrows():
    print(col['Name'], "--", col['Age'])

print("\n Example itertuples \n")
for row in employees.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), "--", getattr(row, "Age"))

### 14如何通过名称或索引删除 DataFrame 的列
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print(employees)

print("\n Drop Column by Name \n")
employees.drop('Age', axis=1, inplace=True)
print(employees)

print("\n Drop Column by Index \n")
employees.drop(employees.columns[[0, 1]], axis=1, inplace=True)
print(employees)

### 15向 DataFrame 中新增列
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})
employees['City'] = ['London', 'Tokyo', 'Sydney', 'London', 'Toronto']
print(employees)

### 16如何从 DataFrame 中获取列标题列表
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print(list(employees))
print(list(employees.columns.values))
print(employees.columns.tolist())

###  17如何随机生成 DataFrame
np.random.seed(5)
df_random = pd.DataFrame(np.random.randint(100, size=(10, 6)),
                         columns=list('ABCDEF'),
                         index=['Row-{}'.format(i) for i in range(10)])
print(df_random)

###  18如何选择 DataFrame 的多个列
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

df = employees[['EmpCode', 'Age', 'Name']]
print(df)

###  19如何将字典转换为 DataFrame
data = ({'Age': [30, 20, 22, 40, 32, 28, 39],
         'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                   'Red'],
         'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                  'Melon', 'Beans'],
         'Height': [165, 70, 120, 80, 180, 172, 150],
         'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
         'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
         })
print(data)

df = pd.DataFrame(data)
print(df)

###  20使用 ioc 进行切片
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean','Christina', 'Cornelia'])

print("\n -- Selecting a single row with .loc with a string -- \n")
print(df.loc['Penelope'])

print("\n -- Selecting multiple rows with .loc with a list of strings -- \n")
print(df.loc[['Cornelia', 'Jane', 'Dean']])

print("\n -- Selecting multiple rows with .loc with slice notation -- \n")
print(df.loc['Aaron':'Dean'])

###  21检查 DataFrame 中是否是空的
df = pd.DataFrame()
if df.empty:
    print('DataFrame is empty!')

###  22在创建 DataFrame 时指定索引和列名称
values = ["India", "Canada", "Australia","Japan", "Germany", "France"]
code = ["IND", "CAN", "AUS", "JAP", "GER", "FRA"]
df = pd.DataFrame(values, index=code, columns=['Country'])
print(df)

###  23使用 iloc 进行切片
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black','Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese','Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'])

print("\n -- Selecting a single row with .iloc with an integer -- \n")
print(df.iloc[4])

print("\n -- Selecting multiple rows with .iloc with a list of integers -- \n")
print(df.iloc[[2, -2]])

print("\n -- Selecting multiple rows with .iloc with slice notation -- \n")
print(df.iloc[:5:3])

###  24iloc 和 loc 的区别
# loc 索引器还可以进行布尔选择，例如，如果我们想查找 Age 小于 30 的所有行并仅返回 Color 和 Height 列，我们可以执行以下操作。我们可以用 iloc 复制它，但我们不能将它传递给一个布尔系列，必须将布尔系列转换为 numpy 数组
# loc 从索引中获取具有特定标签的行（或列）
# iloc 在索引中的特定位置获取行（或列）（因此它只需要整数）
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n -- loc -- \n")
print(df.loc[df['Age'] < 30, ['Color', 'Height']])

print("\n -- iloc -- \n")
print(df.iloc[(df['Age'] < 30).values, [1, 3]])

###  25使用时间索引创建空 DataFrame
todays_date = datetime.datetime.now().date()
index = pd.date_range(todays_date, periods=10, freq='D')

columns = ['A', 'B', 'C']

df = pd.DataFrame(index=index, columns=columns)
df = df.fillna(0)

print(df)

###  26如何改变 DataFrame 列的排序
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n -- Change order using columns -- \n")
new_order = [3, 2, 1, 4, 5, 0]
df = df[df.columns[new_order]]
print(df)

print("\n -- Change order using reindex -- \n")
df = df.reindex(['State', 'Color', 'Age', 'Food', 'Score', 'Height'], axis=1)
print(df)

###  27检查 DataFrame 列的数据类型
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.dtypes)

### 28更改 DataFrame 指定列的数据类型
df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.dtypes)
df['Age'] = df['Age'].astype(str)
print(df.dtypes)

### 29如何将列的数据类型转换为 DateTime 类型
df = pd.DataFrame({'DateOFBirth': [1349720105, 1349806505, 1349892905,
                                   1349979305, 1350065705, 1349792905,
                                   1349730105],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n----------------Before---------------\n")
print(df.dtypes)
print(df)

df['DateOFBirth'] = pd.to_datetime(df['DateOFBirth'], unit='s')

print("\n----------------After----------------\n")
print(df.dtypes)
print(df)

### 30将 DataFrame 列从 floats 转为 ints

df = pd.DataFrame({'DailyExp': [75.7, 56.69, 55.69, 96.5, 84.9, 110.5,
                                58.9],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n----------------Before---------------\n")
print(df.dtypes)
print(df)

df['DailyExp'] = df['DailyExp'].astype(int)

print("\n----------------After----------------\n")
print(df.dtypes)
print(df)

###  31如何把dates列转换为DateTime类型
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print("\n----------------Before---------------\n")
print(df.dtypes)

df['DateOfBirth'] = df['DateOfBirth'].astype('datetime64')

print("\n----------------After----------------\n")
print(df.dtypes)

###  32两个DataFrame相加
df1 = pd.DataFrame({'Age': [30, 20, 22, 40], 'Height': [165, 70, 120, 80],
                    'Score': [4.6, 8.3, 9.0, 3.3], 'State': ['NY', 'TX',
                                                             'FL', 'AL']},
                   index=['Jane', 'Nick', 'Aaron', 'Penelope'])

df2 = pd.DataFrame({'Age': [32, 28, 39], 'Color': ['Gray', 'Black', 'Red'],
                    'Food': ['Cheese', 'Melon', 'Beans'],
                    'Score': [1.8, 9.5, 2.2], 'State': ['AK', 'TX', 'TX']},
                   index=['Dean', 'Christina', 'Cornelia'])
df3 = df1.append(df2, sort=True)

print(df3)

###  33在DataFrame末尾添加额外的行
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\n------------ BEFORE ----------------\n")
print(employees)

employees.loc[len(employees)] = [45, '2018-01-25', 'Emp006', 'Sunny',
                                 'Programmer']

print("\n------------ AFTER ----------------\n")
print(employees)

### 34为指定索引添加新行
employees = pd.DataFrame(
    data={'Name': ['John Doe', 'William Spark'],
          'Occupation': ['Chemist', 'Statistician'],
          'Date Of Join': ['2018-01-25', '2018-01-26'],
          'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])

print("\n------------ BEFORE ----------------\n")
print(employees)

employees.loc['Emp003'] = ['Sunny', 'Programmer', '2018-01-25', 45]

print("\n------------ AFTER ----------------\n")
print(employees)

### 35如何使用for 循环添加行
cols = ['Zip']
lst = []
zip = 32100

for a in range(10):
    lst.append([zip])
    zip = zip + 1

df = pd.DataFrame(lst, columns=cols)
print(df)

### 36在DataFrame顶部添加一行
employees = pd.DataFrame({
    'EmpCode': ['Emp002', 'Emp003', 'Emp004'],
    'Name': ['John', 'Doe', 'William'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26'],
    'Age': [23, 24, 34]})

print("\n------------ BEFORE ----------------\n")
print(employees)

# New line
line = pd.DataFrame({'Name': 'Dean', 'Age': 45, 'EmpCode': 'Emp001',
                     'Date Of Join': '2018-02-26', 'Occupation': 'Chemist'
                     }, index=[0])

# Concatenate two dataframe
employees = pd.concat([line, employees.ix[:]]).reset_index(drop=True)

print("\n------------ AFTER ----------------\n")
print(employees)

### 37如何向DataFrame中动态添加行
df = pd.DataFrame(columns=['Name', 'Age'])

df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 23

df.loc[2, 'Name'] = 'Sunny'
print(df)

### 38在任意位置插入行
df = pd.DataFrame(columns=['Name', 'Age'])

df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 21

df.loc[2, 'Name'] = 'Sunny'
df.loc[2, 'Age'] = 22

df.loc[3, 'Name'] = 'Mark'
df.loc[3, 'Age'] = 25

df.loc[4, 'Name'] = 'Taylor'
df.loc[4, 'Age'] = 28

print("\n------------ BEFORE ----------------\n")
print(df)

line = pd.DataFrame({"Name": "Jack", "Age": 24}, index=[2.5])
df = df.append(line, ignore_index=False)
df = df.sort_index().reset_index(drop=True)

df = df.reindex(['Name', 'Age'], axis=1)
print("\n------------ AFTER ----------------\n")
print(df)

### 39使用时间戳索引向DataFrame中添加行
df = pd.DataFrame(columns=['Name', 'Age'])

df.loc['2014-05-01 18:47:05', 'Name'] = 'Rocky'
df.loc['2014-05-01 18:47:05', 'Age'] = 21

df.loc['2014-05-02 18:47:05', 'Name'] = 'Sunny'
df.loc['2014-05-02 18:47:05', 'Age'] = 22

df.loc['2014-05-03 18:47:05', 'Name'] = 'Mark'
df.loc['2014-05-03 18:47:05', 'Age'] = 25

print("\n------------ BEFORE ----------------\n")
print(df)

line = pd.to_datetime("2014-05-01 18:50:05", format="%Y-%m-%d %H:%M:%S")
new_row = pd.DataFrame([['Bunny', 26]], columns=['Name', 'Age'], index=[line])
df = pd.concat([df, pd.DataFrame(new_row)], ignore_index=False)

print("\n------------ AFTER ----------------\n")
print(df)

### 40为不同的行填充缺失值
a = {'A': 10, 'B': 20}
b = {'B': 30, 'C': 40, 'D': 50}

df1 = pd.DataFrame(a, index=[0])
df2 = pd.DataFrame(b, index=[1])

df = pd.DataFrame()
df = df.append(df1)
df = df.append(df2).fillna(0)

print(df)

# 41append, concat和combine_first示例
a = {'A': 10, 'B': 20}
b = {'B': 30, 'C': 40, 'D': 50}

df1 = pd.DataFrame(a, index=[0])
df2 = pd.DataFrame(b, index=[1])

d1 = pd.DataFrame()
d1 = d1.append(df1)
d1 = d1.append(df2).fillna(0)
print("\n------------ append ----------------\n")
print(d1)

d2 = pd.concat([df1, df2]).fillna(0)
print("\n------------ concat ----------------\n")
print(d2)

d3 = pd.DataFrame()
d3 = d3.combine_first(df1).combine_first(df2).fillna(0)
print("\n------------ combine_first ----------------\n")
print(d3)

# 42获取行和列的平均值

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

df['Mean Basket'] = df.mean(axis=1)
df.loc['Mean Fruit'] = df.mean()

print(df)

# 43计算行和列的总和
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

df['Sum Basket'] = df.sum(axis=1)
df.loc['Sum Fruit'] = df.sum()

print(df)

# 44连接两列
df = pd.DataFrame(columns=['Name', 'Age'])

df.loc[1, 'Name'] = 'Rocky'
df.loc[1, 'Age'] = 21

df.loc[2, 'Name'] = 'Sunny'
df.loc[2, 'Age'] = 22

df.loc[3, 'Name'] = 'Mark'
df.loc[3, 'Age'] = 25

df.loc[4, 'Name'] = 'Taylor'
df.loc[4, 'Age'] = 28

print('\n------------ BEFORE ----------------\n')
print(df)

df['Employee'] = df['Name'].map(str) + ' - ' + df['Age'].map(str)
df = df.reindex(['Employee'], axis=1)

print('\n------------ AFTER ----------------\n')
print(df)

### 45过滤包含某字符串的行
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])
print(df)

print("\n---- Filter with State contains TX ----\n")
df1 = df[df['State'].str.contains("TX")]

print(df1)

### 46过滤索引中包含某字符串的行
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
print(df)
print("\n---- Filter Index contains ane ----\n")
df.index = df.index.astype('str')
df1 = df[df.index.str.contains('ane')]

print(df1)

### 47使用AND运算符过滤包含特定字符串值的行
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
print(df)

print("\n---- Filter DataFrame using & ----\n")

df.index = df.index.astype('str')
df1 = df[df.index.str.contains('ane') & df['State'].str.contains("TX")]

print(df1)

### 48查找包含某字符串的所有行

df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
print(df)

print("\n---- Filter DataFrame using & ----\n")

df.index = df.index.astype('str')
df1 = df[df.index.str.contains('ane') | df['State'].str.contains("TX")]

print(df1)

### 49如果行中的值包含字符串，则创建与字符串相等的另一列
df = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Accountant', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

df['Department'] = pd.np.where(df.Occupation.str.contains("Chemist"), "Science",
                               pd.np.where(df.Occupation.str.contains("Statistician"), "Economics",
                                           pd.np.where(df.Occupation.str.contains("Programmer"), "Computer",
                                                       "General")))

print(df)

### 50计算pandas group中每组的行数
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0],
                   [6, 6, 6, 6], [8, 8, 8, 8], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Rice', 'Oil'],
                  index=['Basket1', 'Basket2', 'Basket3',
                         'Basket4', 'Basket5', 'Basket6'])

print(df)
print("\n ----------------------------- \n")
print(df[['Apple', 'Orange', 'Rice', 'Oil']].
      groupby(['Apple']).agg(['mean', 'count']))

### 51检查字符串是否在DataFrme中
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])

if df['State'].str.contains('TX').any():
    print("TX is there")

### 52从DataFrame列中获取唯一行值

df = pd.DataFrame({'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df)
print("\n----------------\n")

print(df["State"].unique())

### 53计算DataFrame列的不同值
df = pd.DataFrame({'Age': [30, 20, 22, 40, 20, 30, 20, 25],
                   'Height': [165, 70, 120, 80, 162, 72, 124, 81],
                   'Score': [4.6, 8.3, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'TX', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Jaane', 'Nicky', 'Armour', 'Ponting'])

print(df.Age.value_counts())

### 54删除具有重复索引的行
df = pd.DataFrame({'Age': [30, 30, 22, 40, 20, 30, 20, 25],
                   'Height': [165, 165, 120, 80, 162, 72, 124, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print("\n -------- Duplicate Rows ----------- \n")
print(df)

df1 = df.reset_index().drop_duplicates(subset='index',
                                       keep='first').set_index('index')

print("\n ------- Unique Rows ------------ \n")
print(df1)

### 55删除某些列具有重复值的行
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print("\n -------- Duplicate Rows ----------- \n")
print(df)

df1 = df.reset_index().drop_duplicates(subset=['Age', 'Height'],
                                       keep='first').set_index('index')

print("\n ------- Unique Rows ------------ \n")
print(df1)

### 56从DataFrame单元格中获取值
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print(df.loc['Nicky', 'Age'])

### 57使用DataFrame中的条件索引获取单元格上的标量值

df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81],
                   'Score': [4.6, 4.6, 9.0, 3.3, 4, 8, 9, 3],
                   'State': ['NY', 'NY', 'FL', 'AL', 'NY', 'TX', 'FL', 'AL']},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])

print("\nGet Height where Age is 20")
print(df.loc[df['Age'] == 20, 'Height'].values[0])

print("\nGet State where Age is 30")
print(df.loc[df['Age'] == 30, 'State'].values[0])

### 58设置DataFrame的特定单元格值
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81]},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
print("\n--------------Before------------\n")
print(df)

df.iat[0, 0] = 90
df.iat[0, 1] = 91
df.iat[1, 1] = 92
df.iat[2, 1] = 93
df.iat[7, 1] = 99

print("\n--------------After------------\n")
print(df)

### 59从DataFrame行获取单元格值
df = pd.DataFrame({'Age': [30, 40, 30, 40, 30, 30, 20, 25],
                   'Height': [120, 162, 120, 120, 120, 72, 120, 81]},
                  index=['Jane', 'Jane', 'Aaron', 'Penelope', 'Jaane', 'Nicky',
                         'Armour', 'Ponting'])
print(df.loc[df.Age == 30, 'Height'].tolist())

### 60用字典替换DataFrame列中的值
df = pd.DataFrame({'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']},
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia'])

print(df)

dict = {"NY": 1, "TX": 2, "FL": 3, "AL": 4, "AK": 5}
df1 = df.replace({"State": dict})

print("\n\n")
print(df1)

### 61统计基于某一列的一列的数值
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df.groupby('State').DateOfBirth.nunique())

### 62处理DataFrame中的缺失值

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, ]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame ---------\n")
print(df)

print("\n--------- Use of isnull() ---------\n")
print(df.isnull())

print("\n--------- Use of notnull() ---------\n")
print(df.notnull())

### 63删除包含任何缺失数据的行
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, ]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame ---------\n")
print(df)

print("\n--------- Use of dropna() ---------\n")
print(df.dropna())

### 64删除DataFrame中缺失数据的列

df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, ]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame ---------\n")
print(df)

print("\n--------- Drop Columns) ---------\n")
print(df.dropna(1))

### 65按降序对索引值进行排序

df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])

print(df.sort_index(ascending=False))

### 66按降序对列进行排序
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print(employees.sort_index(axis=1, ascending=False))

### 67使用rank方法查找DataFrame中元素的排名
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [5, 5, 0, 0]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print("\n--------- DataFrame Values--------\n")
print(df)

print("\n--------- DataFrame Values by Rank--------\n")
print(df.rank())

### 68在多列上设置索引
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

print("\n --------- Before Index ----------- \n")
print(employees)

print("\n --------- Multiple Indexing ----------- \n")
print(employees.set_index(['Occupation', 'Age']))

### 69确定DataFrame的周期索引和列
values = ["India", "Canada", "Australia",
          "Japan", "Germany", "France"]
pidx = pd.period_range('2015-01-01', periods=6)
df = pd.DataFrame(values, index=pidx, columns=['Country'])
print(df)

### 70导入CSV指定特定索引
df = pd.read_csv('test.csv', index_col="DateTime")
print(df)

### 71将DataFrame写入csv
df = pd.DataFrame({'DateOfBirth': ['1986-11-11', '1999-05-12', '1976-01-01',
                                   '1986-06-01', '1983-06-04', '1990-03-07',
                                   '1999-07-09'],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Pane', 'Aaron', 'Penelope', 'Frane',
                         'Christina', 'Cornelia'])
df.to_csv('test.csv', encoding='utf-8', index=True)

### 72使用Pandas读取csv文件的特定列
df = pd.read_csv("test.csv", usecols=['Wheat', 'Oil'])
print(df)

### 73Pandas获取CSV列的列表
cols = list(pd.read_csv("test.csv", nrows=1))
print(cols)

### 74找到列值最大的行
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print(df.ix[df['Apple'].idxmax()])

### 75使用查询方法进行复杂条件选择
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

print(df)

print("\n ----------- Filter data using query method ------------- \n")
df1 = df.ix[df.query('Apple > 50 & Orange <= 15 & Banana < 15 & Pear == 12').index]
print(df1)

### 76检查Pandas中是否存在列
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3'])

if 'Apple' in df.columns:
    print("Yes")
else:
    print("No")

if set(['Apple', 'Orange']).issubset(df.columns):
    print("Yes")
else:
    print("No")

### 77为特定列从DataFrame中查找n - smallest和n - largest值
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- nsmallest -----------\n")
print(df.nsmallest(2, ['Apple']))

print("\n----------- nlargest -----------\n")
print(df.nlargest(2, ['Apple']))

### 78从DataFrame中查找所有列的最小值和最大值
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Minimum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].min())

print("\n----------- Maximum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].max())

### 79在DataFrame中找到最小值和最大值所在的索引位置
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Minimum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].idxmin())

print("\n----------- Maximum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].idxmax())

### 80计算DataFrameColumns的累积乘积和累积总和
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Cumulative Product -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].cumprod())

print("\n----------- Cumulative Sum -----------\n")
print(df[['Apple', 'Orange', 'Banana', 'Pear']].cumsum())

### 81汇总统计
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Describe DataFrame -----------\n")
print(df.describe())

print("\n----------- Describe Column -----------\n")
print(df[['Apple']].describe())

### 82查找DataFrame的均值、中值和众数
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Calculate Mean -----------\n")
print(df.mean())

print("\n----------- Calculate Median -----------\n")
print(df.median())

print("\n----------- Calculate Mode -----------\n")
print(df.mode())

### 83测量DataFrame列的方差和标准偏差
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Calculate Mean -----------\n")
print(df.mean())

print("\n----------- Calculate Median -----------\n")
print(df.median())

print("\n----------- Calculate Mode -----------\n")
print(df.mode())

### 84计算DataFrame列之间的协方差
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n----------- Calculating Covariance -----------\n")
print(df.cov())

print("\n----------- Between 2 columns -----------\n")
# Covariance of Apple vs Orange
print(df.Apple.cov(df.Orange))

### 85计算Pandas中两个DataFrame对象之间的相关性
df1 = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                    [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                   columns=['Apple', 'Orange', 'Banana', 'Pear'],
                   index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                          'Basket5', 'Basket6'])

print("\n------ Calculating Correlation of one DataFrame Columns -----\n")
print(df1.corr())

df2 = pd.DataFrame([[52, 54, 58, 41], [14, 24, 51, 78], [55, 15, 8, 12],
                    [15, 14, 1, 8], [7, 17, 18, 98], [15, 34, 29, 52]],
                   columns=['Apple', 'Orange', 'Banana', 'Pear'],
                   index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                          'Basket5', 'Basket6'])

print("\n----- Calculating correlation between two DataFrame -------\n")
print(df2.corrwith(other=df1))

### 86计算DataFrame列的每个单元格的百分比变化
df = pd.DataFrame([[10, 20, 30, 40], [7, 14, 21, 28], [55, 15, 8, 12],
                   [15, 14, 1, 8], [7, 1, 1, 8], [5, 4, 9, 2]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n------ Percent change at each cell of a Column -----\n")
print(df[['Apple']].pct_change()[:3])

print("\n------ Percent change at each cell of a DataFrame -----\n")
print(df.pct_change()[:5])

### 87在Pandas中向前和向后填充DataFrame列的缺失值
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n------ DataFrame with NaN -----\n")
print(df)

print("\n------ DataFrame with Forward Filling -----\n")
print(df.ffill())

print("\n------ DataFrame with Forward Filling -----\n")
print(df.bfill())

### 88在Pandas中使用非分层索引使用Stacking
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n------ DataFrame-----\n")
print(df)

print("\n------ Stacking DataFrame -----\n")
print(df.stack(level=-1))

### 89使用分层索引对Pandas进行拆分
df = pd.DataFrame([[10, 30, 40], [], [15, 8, 12],
                   [15, 14, 1, 8], [7, 8], [5, 4, 1]],
                  columns=['Apple', 'Orange', 'Banana', 'Pear'],
                  index=['Basket1', 'Basket2', 'Basket3', 'Basket4',
                         'Basket5', 'Basket6'])

print("\n------ DataFrame-----\n")
print(df)

print("\n------ Unstacking DataFrame -----\n")
print(df.unstack(level=-1))

# 90Pandas获取HTML页面上table数据

# df
pd.read_html("url")