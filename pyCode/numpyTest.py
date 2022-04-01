import numpy as np
import random

# 文章引用：https://mp.weixin.qq.com/s/9CrgsQsPVw4I9rkC-931Fg

# 1有多个条件时替换 Numpy 数组中的元素
# 将所有大于 30 的元素替换为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])

an_array = np.where(the_array > 30, 0, the_array)
print(an_array)

# 将大于 30 小于 50 的所有元素替换为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where((the_array > 30) & (the_array < 50), 0, the_array)
print(an_array)

# 给所有大于 40 的元素加 5
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 40, the_array + 5, the_array)
print(an_array)

# 用 Nan 替换数组中大于 25 的所有元素
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 25, np.NaN, the_array)
print(an_array)

# 将数组中大于 25 的所有元素替换为 1，否则为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.asarray([0 if val < 25 else 1 for val in the_array])
print(an_array)

# 2在 Python 中找到 Numpy 数组的维度
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.ndim)

arr = np.array([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]])
print(arr.ndim)

arr = np.array([[[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]])
print(arr.ndim)

# 3两个条件过滤 NumPy 数组
#Example 1

the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = np.logical_and(np.greater(the_array, 3), np.less(the_array, 8))
print(the_array[filter_arr])

#Example 2
the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = np.logical_or(the_array < 3, the_array == 4)
print(the_array[filter_arr])

#Example 3
the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = np.logical_not(the_array > 1, the_array < 5)
print(the_array[filter_arr])

#Example 4
the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = np.logical_or(the_array == 8, the_array < 5)
print(the_array[filter_arr])

#Example 5
the_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
filter_arr = np.logical_and(the_array == 8, the_array < 5)
print(the_array[filter_arr])

# 4对最后一列求和
# 第一列总和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
column_sums = newarr[:, 0].sum()
print(column_sums)

# 第二列总和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

column_sums = newarr[:, 1].sum()
print(column_sums)

# 第一列和第二列的总和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
column_sums = newarr[:, 0:2].sum()
print(column_sums)

# 最后一列的总和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
column_sums = newarr[:, -1].sum()
print(column_sums)

# 5满足条件，则替换 Numpy 元素
# 将所有大于 30 的元素替换为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 30, 0, the_array)
print(an_array)

# 将大于 30 小于 50 的所有元素替换为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where((the_array > 30) & (the_array < 50), 0, the_array)
print(an_array)

# 给所有大于 40 的元素加 5
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 40, the_array + 5, the_array)
print(an_array)

# 用 Nan 替换数组中大于 25 的所有元素
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 25, np.NaN, the_array)
print(an_array)

# 将数组中大于 25 的所有元素替换为 1，否则为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.asarray([0 if val < 25 else 1 for val in the_array])
print(an_array)

# 6从 Nump y数组中随机选择两行
#Example 1

# create 2D array
the_array = np.arange(50).reshape((5, 10))

# row manipulation
np.random.shuffle(the_array)

# display random rows
rows = the_array[:2, :]
print(rows)

#Example 2

# create 2D array
the_array = np.arange(16).reshape((4, 4))

# row manipulation
rows_id = random.sample(range(0, the_array.shape[1] - 1), 2)

# display random rows
rows = the_array[rows_id, :]

#Example 3

# create 2D array
the_array = np.arange(16).reshape((4, 4))

number_of_rows = the_array.shape[0]
random_indices = np.random.choice(number_of_rows,
                                  size=2,
                                  replace=False)

# display random rows
rows = the_array[random_indices, :]
print(rows)

# 7以给定的精度漂亮地打印一个 Numpy 数组
#Example 1
x = np.array([[1.1, 0.9, 1e-6]] * 3)
print(x)
print(np.array_str(x, precision=1, suppress_small=True))

#Example 2
x = np.random.random(10)
print(x)

np.set_printoptions(precision=3)
print(x)

#Example 3
x = np.array([[1.1, 0.9, 1e-6]] * 3)
print(x)

np.set_printoptions(suppress=True)
print(x)

#Example 4
x = np.array([[1.1, 0.9, 1e-6]] * 3)
print(x)

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
print(x)

#Example 5
x = np.random.random((3, 3)) * 9
print(np.array2string(x, formatter={'float_kind': '{0:.3f}'.format}))

# 8提取 Numpy 矩阵的前 n 列
# 列范围1
the_arr = np.array([[0, 1, 2, 3, 5, 6, 7, 8],
                    [4, 5, 6, 7, 5, 3, 2, 5],
                    [8, 9, 10, 11, 4, 5, 3, 5]])
print(the_arr[:, 1:5])

# 列范围2
the_arr = np.array([[0, 1, 2, 3, 5, 6, 7, 8],
                    [4, 5, 6, 7, 5, 3, 2, 5],
                    [8, 9, 10, 11, 4, 5, 3, 5]])
print(the_arr[:, np.r_[0:1, 5]])

# 列范围3
the_arr = np.array([[0, 1, 2, 3, 5, 6, 7, 8],
                    [4, 5, 6, 7, 5, 3, 2, 5],
                    [8, 9, 10, 11, 4, 5, 3, 5]])
print(the_arr[:, np.r_[:1, 3, 7:8]])

# 特定列
the_arr = np.array([[0, 1, 2, 3, 5, 6, 7, 8],
                    [4, 5, 6, 7, 5, 3, 2, 5],
                    [8, 9, 10, 11, 4, 5, 3, 5]])
print(the_arr[:, 1])

# 特定行和列
the_arr = np.array([[0, 1, 2, 3, 5, 6, 7, 8],
                    [4, 5, 6, 7, 5, 3, 2, 5],
                    [8, 9, 10, 11, 4, 5, 3, 5]])
print(the_arr[0:2, 1:3])

# 9从 NumPy 数组中删除值
#Example 1
the_array = np.array([[1, 2], [3, 4]])
print(the_array)

the_array = np.delete(the_array, [1, 2])
print(the_array)

#Example 2
the_array = np.array([1, 2, 3, 4])
print(the_array)

the_array = np.delete(the_array, np.where(the_array == 2))
print(the_array)

#Example 3
the_array = np.array([[1, 2], [3, 4]])
print(the_array)

the_array = np.delete(the_array, np.where(the_array == 3))
print(the_array)

# 10将满足条件的项目替换为 Numpy 数组中的另一个值
# 将所有大于 30 的元素替换为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 30, 0, the_array)
print(an_array)

# 将大于 30 小于 50 的所有元素替换为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where((the_array > 30) & (the_array < 50), 0, the_array)
print(an_array)

# 给所有大于 40 的元素加 5
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 40, the_array + 5, the_array)
print(an_array)

# 用 Nan 替换数组中大于 25 的所有元素
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.where(the_array > 25, np.NaN, the_array)

# 将数组中大于 25 的所有元素替换为 1，否则为 0
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
an_array = np.asarray([0 if val < 25 else 1 for val in the_array])
print(an_array)

# 11对 NumPy 数组中的所有元素求和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
column_sums = newarr[:, :].sum()
print(column_sums)

# 12创建 3D NumPy 零数组
the_3d_array = np.zeros((2, 2, 2))
print(the_3d_array)

# 13计算 NumPy 数组中每一行的总和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)
print(newarr)

column_sums = newarr.sum(axis=1)

# 14打印没有科学记数法的 NumPy 数组
np.set_printoptions(suppress=True,
                    formatter={'float_kind': '{:f}'.format})

the_array = np.array([3.74, 5162, 13683628846.64, 12783387559.86, 1.81])
print(the_array)

# 15获取numpy数组中所有NaN值的索引列表
the_array = np.array([np.nan, 2, 3, 4])
array_has_nan = np.isnan(the_array)
print(array_has_nan)

# 16检查 NumPy 数组中的所有元素都是 NaN

the_array = np.array([np.nan, 2, 3, 4])
array_has_nan = np.isnan(the_array).all()
print(array_has_nan)

the_array = np.array([np.nan, np.nan, np.nan, np.nan])
array_has_nan = np.isnan(the_array).all()
print(array_has_nan)

# 17将列表添加到 Python 中的 NumPy 数组
the_array = np.array([[1, 2], [3, 4]])
columns_to_append = [5, 6]
the_array = np.insert(the_array, 2, columns_to_append, axis=1)
print(the_array)

# 18在 Numpy 中抑制科学记数法
np.set_printoptions(suppress=True,
                    formatter={'float_kind': '{:f}'.format})

the_array = np.array([3.74, 5162, 13683628846.64, 12783387559.86, 1.81])
print(the_array)

# 19将具有 12 个元素的一维数组转换为 3 维数组
#Example 1
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#Example 2
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2)
print(newarr)

#Example 3
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2).transpose()
print(newarr)

#Example 4
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(-1, 2).T.reshape(-1, 3, 4)
print(newarr)

# 20检查 NumPy 数组是否为空
the_array = np.array([])
is_empty = the_array.size == 0
print(is_empty)
the_array = np.array([1, 2, 3])
is_empty = the_array.size == 0
print(is_empty)

# 21在 Python 中重塑 3D 数组
#Example 1
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

#Example 2
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2)
print(newarr)

#Example 3
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 2, 2).transpose()
print(newarr)

#Example 4
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(-1, 2).T.reshape(-1, 3, 4)
print(newarr)

# 22在 Python 中重复 NumPy 数组中的一列
the_array = np.array([1, 2, 3])
repeat = 3

new_array = np.transpose([the_array] * repeat)
print(new_array)

# 23在 NumPy 数组中找到跨维度的平均值
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array.mean(axis=0)
print(mean_array)

# 24检查 NumPy 数组中的 NaN 元素
the_array = np.array([np.nan, 2, 3, 4])
array_has_nan = np.isnan(the_array).any()
print(array_has_nan)

the_array = np.array([1, 2, 3, 4])
array_has_nan = np.isnan(the_array).any()
print(array_has_nan)

# 25格式化 NumPy 数组的打印方式
#Example 1
x = np.array([[1.1, 0.9, 1e-6]] * 3)
print(x)
print(np.array_str(x, precision=1, suppress_small=True))

#Example 2
x = np.random.random(10)
print(x)
np.set_printoptions(precision=3)
print(x)

#Example 3
x = np.array([[1.1, 0.9, 1e-6]] * 3)
print(x)
np.set_printoptions(suppress=True)
print(x)

#Example 4
x = np.array([[1.1, 0.9, 1e-6]] * 3)
print(x)
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
print(x)

#Example 5
x = np.random.random((3, 3)) * 9
print(np.array2string(x, formatter={'float_kind': '{0:.3f}'.format}))

# 26乘以Numpy数组的每个元素
#Example 1
the_array = np.array([[1, 2, 3], [1, 2, 3]])
prod = np.prod(the_array)
print(prod)

#Example 2
the_array = np.array([[1, 2, 3], [1, 2, 3]])
prod = np.prod(the_array, 0)
print(prod)

#Example 3
the_array = np.array([[1, 2, 3], [1, 2, 3]])
prod = np.prod(the_array, 1)
print(prod)

#Example 4
the_array = np.array([1, 2, 3])
prod = np.prod(the_array)
print(prod)

# 27在 NumPy 中生成随机数
#Example 1
# create 2D array
the_array = np.arange(50).reshape((5, 10))

# row manipulation
np.random.shuffle(the_array)

# display random rows
rows = the_array[:2, :]
print(rows)

#Example 2
# create 2D array
the_array = np.arange(16).reshape((4, 4))

# row manipulation
rows_id = random.sample(range(0, the_array.shape[1] - 1), 2)

# display random rows
rows = the_array[rows_id, :]

#Example 3
# create 2D array
the_array = np.arange(16).reshape((4, 4))

number_of_rows = the_array.shape[0]
random_indices = np.random.choice(number_of_rows,
                                  size=2,
                                  replace=False)
# display random rows
rows = the_array[random_indices, :]
print(rows)

# 28Numpy 将具有 8 个元素的一维数组转换为 Python 中的二维数组
# 4 行 2 列
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(4, 2)
print(newarr)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 4)
print(newarr)

# 29在 Python 中使用 numpy.all()
thelist = [[True, True], [True, True]]
thebool = np.all(thelist)
print(thebool)

thelist = [[False, False], [False, False]]
thebool = np.all(thelist)
print(thebool)

thelist = [[True, False], [True, False]]
thebool = np.all(thelist)
print(thebool)

# 30将一维数组转换为二维数组4 行 2 列
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(4, 2)
print(newarr)

# 2 行 4 列
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 4)
print(newarr)

#Example 3
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.reshape(arr, (-1, 2))
print(newarr)


#Example 4 通过添加新轴将一维数组转换为二维数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.reshape(arr, (1, arr.size))
print(newarr)

#Example 5
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.reshape(arr, (-1, 4))
print(newarr)

# 31计算 NumPy 数组中唯一值的频率
the_array = np.array([9, 7, 4, 7, 3, 5, 9])
frequencies = np.asarray((np.unique(the_array, return_counts=True))).T
print(frequencies)

# 32在一列中找到平均值
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array.mean(axis=0)
print(mean_array)

# 33在 Numpy 数组的长度、维度、大小
#Example 1
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr.ndim,arr.shape)

arr = np.array([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]])
print(arr.ndim,arr.shape)

arr = np.array([[[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]]])
print(arr.ndim,arr.shape)

#Example 2
arr = np.array([[1, 1, 1, 0], [0, 5, 0, 1], [2, 1, 3, 10]])
print(np.info(arr))

# 34在 NumPy 数组中找到最大值的索引
the_array = np.array([11, 22, 53, 14, 15])
max_index_col = np.argmax(the_array, axis=0)
print(max_index_col)

# 35按降序对 NumPy 数组进行排序
# 按降序对 Numpy 进行排序
the_array = np.array([49, 7, 44, 27, 13, 35, 71])
sort_array = np.sort(the_array)[::-1]
print(sort_array)

# 按降序对 2D Numpy 进行排序
the_array = np.array([[49, 7, 4], [27, 13, 35]])
sort_array = np.sort(the_array)[::1]
print(sort_array)

# 按降序对 Numpy 进行排序
the_array = np.array([[49, 7, 4], [27, 13, 35], [12, 3, 5]])
a_idx = np.argsort(-the_array)
sort_array = np.take_along_axis(the_array, a_idx, axis=1)
print(sort_array)

# 36Numpy 从二维数组中获取随机的一组行
#Example 1
# create 2D array
the_array = np.arange(50).reshape((5, 10))
# row manipulation
np.random.shuffle(the_array)
# display random rows
rows = the_array[:2, :]
print(rows)

#Example 2
# create 2D array
the_array = np.arange(16).reshape((4, 4))
# row manipulation
rows_id = random.sample(range(0, the_array.shape[1] - 1), 2)
# display random rows
rows = the_array[rows_id, :]
print(rows)

#Example 3
# create 2D array
the_array = np.arange(16).reshape((4, 4))
number_of_rows = the_array.shape[0]
random_indices = np.random.choice(number_of_rows,
                                  size=2,
                                  replace=False)
# display random rows
rows = the_array[random_indices, :]
print(rows)

# 37将 Numpy 数组转换为 JSON
the_array = np.array([[49, 7, 44], [27, 13, 35], [27, 13, 35]])
lists = the_array.tolist()
print([{'x': x[0], 'y': x[1], 'z': x[2]} for i, x in enumerate(lists)])

# 38检查 NumPy 数组中是否存在值
the_array = np.array([[1, 2], [3, 4]])
n = 3
if n in the_array:
    print(True)
else:
    print(False)

# 39创建一个 3D NumPy 数组
the_3d_array = np.ones((2, 2, 2))
print(the_3d_array)

# 40在numpy中将字符串数组转换为浮点数数组
string_arr = np.array(['1.1', '2.2', '3.3'])
float_arr = string_arr.astype(np.float64)
print(float_arr)

# 41从 Python 的 numpy 数组中随机选择
#Example 1
# create 2D array
the_array = np.arange(50).reshape((5, 10))
# row manipulation
np.random.shuffle(the_array)
# display random rows
rows = the_array[:2, :]
print(rows)

#Example 2
# create 2D array
the_array = np.arange(16).reshape((4, 4))
# row manipulation
rows_id = random.sample(range(0, the_array.shape[1] - 1), 2)
# display random rows
rows = the_array[rows_id, :]
print(rows)

#Example 3
# create 2D array
the_array = np.arange(16).reshape((4, 4))
number_of_rows = the_array.shape[0]
random_indices = np.random.choice(number_of_rows,
                                  size=2,
                                  replace=False)

# display random rows
rows = the_array[random_indices, :]
print(rows)

# 42不截断地打印完整的 NumPy 数组
np.set_printoptions(threshold=np.inf)
the_array = np.arange(100)
print(the_array)

# 43将 Numpy 转换为列表
the_array = np.array([[1, 2], [3, 4]])
print(the_array.tolist())

# 44将字符串数组转换为浮点数数组
string_arr = np.array(['1.1', '2.2', '3.3'])
float_arr = string_arr.astype(np.float64)
print(float_arr)

# 45计算 NumPy 数组中每一列的总和
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
column_sums = newarr.sum(axis=0)
print(column_sums)

# 46使用 Python 中的值创建 3D NumPy 数组
the_3d_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(the_3d_array)

# 47计算不同长度的 Numpy 数组的平均值
x = np.array([[1, 2], [3, 4]])
y = np.array([[1, 2, 3], [3, 4, 5]])
z = np.array([[7], [8]])

arr = np.ma.empty((2, 3, 3))
arr.mask = True
arr[:x.shape[0], :x.shape[1], 0] = x
arr[:y.shape[0], :y.shape[1], 1] = y
arr[:z.shape[0], :z.shape[1], 2] = z
print(arr.mean(axis=2))

# 48从 Numpy 数组中删除 nan 值
#Example 1
x = np.array([np.nan, 2, 3, 4])
x = x[~np.isnan(x)]
print(x)

#Example 2
x = np.array([
    [5, np.nan],
    [np.nan, 0],
    [1, 2],
    [3, 4]
])

x = x[~np.isnan(x).any(axis=1)]
print(x)

# 49向 NumPy 数组添加一列
the_array = np.array([[1, 2], [3, 4]])
columns_to_append = np.array([[5], [6]])
the_array = np.append(the_array, columns_to_append, 1)
print(the_array)

# 50在 Numpy Array 中打印浮点值时如何抑制科学记数法
np.set_printoptions(suppress=True,
                    formatter={'float_kind': '{:f}'.format})

the_array = np.array([3.74, 5162, 13683628846.64, 12783387559.86, 1.81])
print(the_array)

# 51Numpy 将 1d 数组重塑为 1 列的 2d 数组
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(arr.shape[0], -1)
print(newarr)

# 52初始化 NumPy 数组
thearray = np.array([[1, 2], [3, 4], [5, 6]])
print(thearray)

# 53创建重复一行
the_array = np.array([1, 2, 3])
repeat = 3
new_array = np.tile(the_array, (repeat, 1))
print(new_array)

# 54将 NumPy 数组附加到 Python 中的空数组
the_array = np.array([1, 2, 3, 4])
empty_array = np.array([])

new_array = np.append(empty_array, the_array)
print(new_array)

# 55找到 Numpy 数组的平均值
# 计算每列的平均值
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array.mean(axis=0)
print(mean_array)

# 计算每一行的平均值
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array.mean(axis=1)
print(mean_array)

# 仅第一列的平均值
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array[:, 0].mean()
print(mean_array)

# 仅第二列的平均值
the_array = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
mean_array = the_array[:, 0].mean()
print(mean_array)

# 56检测 NumPy 数组是否包含至少一个非数字值
the_array = np.array([np.nan, 2, 3, 4])
array_has_nan = np.isnan(the_array).any()
print(array_has_nan)

the_array = np.array([1, 2, 3, 4])
array_has_nan = np.isnan(the_array).any()
print(array_has_nan)

# 57在 Python 中附加 NumPy 数组
the_array = np.array([[0, 1], [2, 3]])
row_to_append = np.array([[4, 5]])
the_array = np.append(the_array, row_to_append, 0)
print(the_array)
print('*' * 10)
columns_to_append = np.array([[7], [8], [9]])
the_array = np.append(the_array, columns_to_append, 1)
print(the_array)

# 58使用 numpy.any()
thearr = [[True, False], [True, True]]
thebool = np.any(thearr)
print(thebool)
thearr = [[False, False], [False, False]]
thebool = np.any(thearr)
print(thebool)

# 59获得 NumPy 数组的转置
the_array = np.array([[1, 2], [3, 4]])
print(the_array)
print(the_array.T)

# 60获取和设置NumPy数组的数据类型
type1 = np.array([1, 2, 3, 4, 5, 6])
type2 = np.array([1.5, 2.5, 0.5, 6])
type3 = np.array(['a', 'b', 'c'])
type4 = np.array(["Canada", "Australia"], dtype='U5')
type5 = np.array([555, 666], dtype=float)

print(type1.dtype)
print(type2.dtype)
print(type3.dtype)
print(type4.dtype)
print(type5.dtype)
print(type4)

# 61获得NumPy数组的形状
array1d = np.array([1, 2, 3, 4, 5, 6])
array2d = np.array([[1, 2, 3], [4, 5, 6]])
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(array1d.shape)
print(array2d.shape)
print(array3d.shape)

# 62获得 1、2 或 3 维 NumPy 数组
array1d = np.array([1, 2, 3, 4, 5, 6])
print(array1d.ndim)  # 1

array2d = np.array([[1, 2, 3], [4, 5, 6]])
print(array2d.ndim)  # 2

array3d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array3d = array3d.reshape(2, 3, 2)
print(array3d.ndim)  # 3

# 63重塑 NumPy 数组
thearray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
thearray = thearray.reshape(2, 4)
print(thearray)

print("-" * 10)
thearray = thearray.reshape(4, 2)
print(thearray)

print("-" * 10)
thearray = thearray.reshape(8, 1)
print(thearray)

# 64调整 NumPy 数组的大小
thearray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
thearray.resize(4)
print(thearray)

print("-" * 10)
thearray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
thearray.resize(2, 4)
print(thearray)

print("-" * 10)
thearray = np.array([1, 2, 3, 4, 5, 6, 7, 8])
thearray.resize(3, 3)
print(thearray)

# 65将 List 或 Tuple 转换为 NumPy 数组
thelist = [1, 2, 3]
print(type(thelist))  # <class 'list'>

array1 = np.array(thelist)
print(type(array1))  # <class 'numpy.ndarray'>

thetuple = ((1, 2, 3))
print(type(thetuple))  # <class 'tuple'>

array2 = np.array(thetuple)
print(type(array2))  # <class 'numpy.ndarray'>

array3 = np.array([thetuple, thelist, array1])
print(array3)

# 66使用 arange 函数创建 NumPy 数组
array1d = np.arange(5)  # 1 row and 5 columns
print(array1d)

array1d = np.arange(0, 12, 2)  # 1 row and 6 columns
print(array1d)

array2d = np.arange(0, 12, 2).reshape(2, 3)  # 2 rows 3 columns
print(array2d)

array3d = np.arange(9).reshape(3, 3)  # 3 rows and columns
print(array3d)

# 67使用 linspace() 创建 NumPy 数组
array1d = np.linspace(1, 12, 2)
print(array1d)

array1d = np.linspace(1, 12, 4)
print(array1d)

array2d = np.linspace(1, 12, 12).reshape(4, 3)
print(array2d)

# 68NumPy 日志空间数组示例
thearray = np.logspace(5, 10, num=10, base=10000000.0, dtype=float)
print(thearray)

# 69创建 Zeros NumPy 数组
array1d = np.zeros(3)
print(array1d)
array2d = np.zeros((2, 4))
print(array2d)

# 70NumPy One 数组示例
array1d = np.ones(3)
print(array1d)

array2d = np.ones((2, 4))
print(array2d)

# 71NumPy 完整数组示例
array1d = np.full((3), 2)
print(array1d)

array2d = np.full((2, 4), 3)
print(array2d)

# 72NumPy Eye 数组示例
array1 = np.eye(3, dtype=int)
print(array1)

array2 = np.eye(5, k=2)
print(array2)

# 73NumPy 生成随机数数组
print(np.random.rand(3, 2))  # Uniformly distributed values.
print(np.random.randn(3, 2))  # Normally distributed values.

# Uniformly distributed integers in a given range.
print(np.random.randint(2, size=10))
print(np.random.randint(5, size=(2, 4)))

# 74NumPy 标识和对角线数组示例
print(np.identity(3))
print(np.diag(np.arange(0, 8, 2)))
print(np.diag(np.diag(np.arange(9).reshape((3,3)))))

# 75NumPy 索引示例
array1d = np.array([1, 2, 3, 4, 5, 6])
print(array1d[0])   # Get first value
print(array1d[-1])  # Get last value
print(array1d[3])   # Get 4th value from first
print(array1d[-5])  # Get 5th value from last

# Get multiple values
print(array1d[[0, -1]])

print("-" * 10)

array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d)
print("-" * 10)

print(array2d[0, 0])   # Get first row first col
print(array2d[0, 1])   # Get first row second col
print(array2d[0, 2])   # Get first row third col

print(array2d[0, 1])   # Get first row second col
print(array2d[1, 1])   # Get second row second col
print(array2d[2, 1])   # Get third row second col

# 76多维数组中的 NumPy 索引
array3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(array3d)

print(array3d[0, 0, 0])
print(array3d[0, 0, 1])
print(array3d[0, 0, 2])

print(array3d[0, 1, 0])
print(array3d[0, 1, 1])
print(array3d[0, 1, 2])

print(array3d[1, 0, 0])
print(array3d[1, 0, 1])
print(array3d[1, 0, 2])

print(array3d[1, 1, 0])
print(array3d[1, 1, 1])
print(array3d[1, 1, 2])

# 77NumPy 单维切片示例
array1d = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array1d[4:])  # From index 4 to last index
print(array1d[:4])  # From index 0 to 4 index
print(array1d[4:7])  # From index 4(included) up to index 7(excluded)
print(array1d[:-1])  # Excluded last element
print(array1d[:-2])  # Up to second last index(negative index)
print(array1d[::-1])  # From last to first in reverse order(negative step)
print(array1d[::-2])  # All odd numbers in reversed order
print(array1d[-2::-2])  # All even numbers in reversed order
print(array1d[::])  # All elements

# 78NumPy 数组中的多维切片
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("-" * 10)
print(array2d[:, 0:2])  # 2nd and 3rd col
print("-" * 10)
print(array2d[1:3, 0:3])  # 2nd and 3rd row
print("-" * 10)
print(array2d[-1::-1, -1::-1])  # Reverse an array

# 79翻转 NumPy 数组的轴顺序
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(array2d)
print("-" * 10)
# Permute the dimensions of an array.
arrayT = np.transpose(array2d)
print(arrayT)
print("-" * 10)
# Flip array in the left/right direction.
arrayFlr = np.fliplr(array2d)
print(arrayFlr)

print("-" * 10)

# Flip array in the up/down direction.
arrayFud = np.flipud(array2d)
print(arrayFud)

print("-" * 10)

# Rotate an array by 90 degrees in the plane specified by axes.
arrayRot90 = np.rot90(array2d)
print(arrayRot90)

# 80NumPy 数组的连接和堆叠
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])
# Stack arrays in sequence horizontally (column wise).
arrayH = np.hstack((array1, array2))
print(arrayH)
print("-" * 10)
# Stack arrays in sequence vertically (row wise).
arrayV = np.vstack((array1, array2))
print(arrayV)

print("-" * 10)

# Stack arrays in sequence depth wise (along third axis).
arrayD = np.dstack((array1, array2))
print(arrayD)

print("-" * 10)

# Appending arrays after each other, along a given axis.
arrayC = np.concatenate((array1, array2))
print(arrayC)

print("-" * 10)

# Append values to the end of an array.
arrayA = np.append(array1, array2, axis=0)
print(arrayA)

print("-" * 10)
arrayA = np.append(array1, array2, axis=1)
print(arrayA)

# 81NumPy 数组的算术运算
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

print(array1 + array2)
print("-" * 20)

print(array1 - array2)
print("-" * 20)

print(array1 * array2)
print("-" * 20)

print(array2 / array1)
print("-" * 40)

print(array1 ** array2)
print("-" * 40)

# 82NumPy 数组上的标量算术运算
array1 = np.array([[10, 20, 30], [40, 50, 60]])

print(array1 + 2)
print("-" * 20)

print(array1 - 5)
print("-" * 20)

print(array1 * 2)
print("-" * 20)

print(array1 / 5)
print("-" * 20)

print(array1 ** 2)
print("-" * 20)

# 83NumPy 初等数学函数
array1 = np.array([[10, 20, 30], [40, 50, 60]])
print(np.sin(array1))
print("-" * 40)

print(np.cos(array1))
print("-" * 40)

print(np.tan(array1))
print("-" * 40)

print(np.sqrt(array1))
print("-" * 40)

print(np.exp(array1))
print("-" * 40)

print(np.log10(array1))
print("-" * 40)

# 84NumPy Element Wise 数学运算

array1 = np.array([[10, 20, 30], [40, 50, 60]])
array2 = np.array([[2, 3, 4], [4, 6, 8]])
array3 = np.array([[-2, 3.5, -4], [4.05, -6, 8]])

print(np.add(array1, array2))
print("-" * 40)

print(np.power(array1, array2))
print("-" * 40)

print(np.remainder((array2), 5))
print("-" * 40)

print(np.reciprocal(array3))
print("-" * 40)

print(np.sign(array3))
print("-" * 40)

print(np.ceil(array3))
print("-" * 40)

print(np.round(array3))
print("-" * 40)

# 85NumPy 聚合和统计函数
array1 = np.array([[10, 20, 30], [40, 50, 60]])

print("Mean: ", np.mean(array1))

print("Std: ", np.std(array1))

print("Var: ", np.var(array1))

print("Sum: ", np.sum(array1))

print("Prod: ", np.prod(array1))

# 86Where 函数的 NumPy 示例
before = np.array([[1, 2, 3], [4, 5, 6]])

# If element is less than 4, mul by 2 else by 3
after = np.where(before < 4, before * 2, before * 3)

print(after)

# 87Select 函数的 NumPy 示例
before = np.array([[1, 2, 3], [4, 5, 6]])

# If element is less than 4, mul by 2 else by 3 【报错】
after = np.select([before < 4, before], [before * 2, before * 3])
print(after)

# 88选择函数的 NumPy 示例
before = np.array([[0, 1, 2], [2, 0, 1], [1, 2, 0]])
choices = [5, 10, 15]

after = np.choose(before, choices)
print(after)
print("-" * 10)

before = np.array([[0, 0, 0], [2, 2, 2], [1, 1, 1]])
choice1 = [5, 10, 15]
choice2 = [8, 16, 24]
choice3 = [9, 18, 27]
after = np.choose(before, (choice1, choice2, choice3))
print(after)

# 89NumPy 逻辑操作，用于根据给定条件从数组中选择性地选取值
thearray = np.array([[10, 20, 30], [14, 24, 36]])
print(np.logical_or(thearray < 10, thearray > 15))
print("-" * 30)
print(np.logical_and(thearray < 10, thearray > 15))
print("-" * 30)
print(np.logical_not(thearray < 20))
print("-" * 30)

# 90标准集合操作的 NumPy 示例
array1 = np.array([[10, 20, 30], [14, 24, 36]])
array2 = np.array([[20, 40, 50], [24, 34, 46]])
# Find the union of two arrays.
print(np.union1d(array1, array2))
# Find the intersection of two arrays.
print(np.intersect1d(array1, array2))
# Find the set difference of two arrays.
print(np.setdiff1d(array1, array2))
