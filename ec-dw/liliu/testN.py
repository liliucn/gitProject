import numpy as np
import pandas as pd
import matplotlib.pyplot as plot

# 文章引用：https://www.runoob.com/numpy/numpy-array-manipulation.html
# region 1、ndarry对象 【ndarry对象：创建一个 ndarray 只需调用 NumPy 的 array 函数即可】
a = np.array([1, 2, 3])  # 一维
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)  # 多维 且 带参数dtype
c = np.array([[(1.5, 2, 3), (4, 5, 6)], [(3, 2, 1), (4, 5, 6)]], dtype=float)  # 多维 且 带参数dtype
print('第一个\n', a, '\n第二个\n', b, '\n第三个\n', c)  # \n 为换行符，前面已经讲过了
# endregion

# region 2、数据类型
# 实例1：使用标量类型
dt = np.dtype(np.int32)
print(dt)

# 实例2：int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

# 实例3：字节顺序标注
dt = np.dtype('<i4')
print(dt)

# 实例4：首先创建结构化数据类型
dt = np.dtype([('age', np.int8)])
print(dt)

# 实例5：将数据类型应用于 ndarray 对象
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a)

# 实例6：类型字段名可以用于存取实际的 age 列
dt = np.dtype([('age', np.int8)])
a = np.array([(10,), (20,), (30,)], dtype=dt)
print(a['age'])

# 实例7：
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
print(student)

# 实例8：
student = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=student)
print(a)

# 每个内建类型都有一个唯一定义它的字符代码，如下：
# 字符	对应类型
# b	布尔型
# i	(有符号) 整型
# u	无符号整型 integer
# f	浮点型
# c	复数浮点型
# m	timedelta（时间间隔）
# M	datetime（日期时间）
# O	(Python) 对象
# S, a	(byte-)字符串
# U	Unicode
# V	原始数据 (void)
# endregion

# region 3、数组属性
# axis=0，表示沿着第 0 轴进行操作，即对每一列进行操作；axis=1，表示沿着第1轴进行操作，即对每一行进行操作。
# NumPy 的数组中比较重要 ndarray 对象属性有：
# 属性	说明
# ndarray.ndim	秩，即轴的数量或维度的数量
# ndarray.shape	数组的维度，对于矩阵，n 行 m 列
# ndarray.size	数组元素的总个数，相当于 .shape 中 n*m 的值
# ndarray.dtype	ndarray 对象的元素类型
# ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
# ndarray.flags	ndarray 对象的内存信息
# ndarray.real	ndarray元素的实部
# ndarray.imag	ndarray 元素的虚部
# ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

# 实例1：
a = np.arange(24)
print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(b.ndim)

# 实例2：
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)

# 实例3：
a = np.array([[1, 2, 3], [4, 5, 6]])
a.shape = (3, 2)
print(a)

# 实例4：
a = np.array([[1, 2, 3], [4, 5, 6]])
b = a.reshape(3, 2)
print(b)

# 实例5：
# 数组的 dtype 为 int8（一个字节）
x = np.array([1, 2, 3, 4, 5], dtype=np.int8)
print(x.itemsize)

# 数组的 dtype 现在为 float64（八个字节）
y = np.array([1, 2, 3, 4, 5], dtype=np.float64)
print(y.itemsize)

# 实例6：ndarray.flags
# ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性：
# 属性	描述
# C_CONTIGUOUS (C)	数据是在一个单一的C风格的连续段中
# F_CONTIGUOUS (F)	数据是在一个单一的Fortran风格的连续段中
# OWNDATA (O)	数组拥有它所使用的内存或从另一个对象中借用它
# WRITEABLE (W)	数据区域可以被写入，将该值设置为 False，则数据为只读
# ALIGNED (A)	数据和所有元素都适当地对齐到硬件上
# UPDATEIFCOPY (U)	这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新
x = np.array([1, 2, 3, 4, 5])
print(x.flags)
# endregion

# region 4、创建数组 numpy.empty、numpy.zeros、numpy.ones

# 实例1
x = np.empty([3, 2], dtype=int)
print(x)
# 实例2
x = np.zeros(5)  # 默认为浮点数
print(x)
y = np.zeros((5,), dtype=np.int)  # 设置类型为整数
print(y)
z = np.zeros((2, 2), dtype=[('x', 'i4'), ('y', 'i4')])  # 自定义类型
print(z)
# 实例3
x = np.ones(5)  # 默认为浮点数
print(x)
x = np.ones([2, 2], dtype=int)  # 自定义类型
print(x)
# endregion

# region 5、从已有的数组创建数组
# 实例1 列表转换为 ndarray:
x = [1, 2, 3]
a = np.asarray(x)
print(a)
# 实例2 元组转换为 ndarray:
x = (1, 2, 3)
a = np.asarray(x)
print(a)
# 实例3 元组列表转换为 ndarray:
x = [(1, 2, 3), (4, 5)]
a = np.asarray(x)
print(a)
# 实例4  设置了 dtype 参数：
x = [1, 2, 3]
a = np.asarray(x, dtype=float)
print(a)
# 实例5 numpy.frombuffer
s = b'Hello World'
a = np.frombuffer(s, dtype='S1')
print(a)
# 实例6  numpy.fromiter 方法从可迭代对象中建立 ndarray 对象，返回一维数组
list = range(5)  # 使用 range 函数创建列表对象
it = iter(list)
x = np.fromiter(it, dtype=float)  # 使用迭代器创建 ndarray
print(x)
# endregion

# region 6、NumPy 从数值范围创建数组
# 实例1 使用 arange 函数创建数值范围并返回 ndarray 对象
x = np.arange(5)
print(x)
# 实例2 设置了 dtype
x = np.arange(5, dtype=float)
print(x)
# 实例3 设置了起始值、终止值及步长：
x = np.arange(10, 20, 2)
print(x)
# 实例4 numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的，格式如下：
a = np.linspace(1, 10, 10)
print(a)
# 实例5 设置元素全部是1的等差数列
a = np.linspace(1, 1, 10)
print(a)
# 实例6 将 endpoint 设为 false，不包含终止值：
a = np.linspace(10, 20, 5, endpoint=False)
print(a)
# 实例7 如果将 endpoint 设为 true，则会包含 20。
a = np.linspace(1, 10, 10, retstep=True)
print(a)
# 实例8 拓展例子
b = np.linspace(1, 10, 10).reshape([10, 1])
print(b)
# 实例9 numpy.logspace 函数用于创建一个于等比数列
# 默认底数是 10
a = np.logspace(1.0, 2.0, num=10)
print(a)
# 将对数的底数设置为 2 :
a = np.logspace(0, 9, 10, base=2)
print(a)
# endregion

# region 7、切片和索引
# 实例1  # 从索引 2 开始到索引 7 停止，间隔为2
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
# 实例2  # 从索引 2 开始到索引 7 停止，间隔为 2
a = np.arange(10)
b = a[2:7:2]
print(b)
# 实例3
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
b = a[5]
print(b)
# 实例4
a = np.arange(10)
print(a[2:])
# 实例5
a = np.arange(10)  # [0 1 2 3 4 5 6 7 8 9]
print(a[2:5])
# 实例6
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a)
# 从某个索引处开始切割
print('从数组索引 a[1:] 处开始切割')
print(a[1:])
# 实例7
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 1])  # 第2列元素
print(a[1, ...])  # 第2行元素
print(a[..., 1:])  # 第2列及剩下的所有元素
# endregion

# region 8、高级索引
# 实例1 整数数组索引
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)
# 实例2 获取了 4X3 数组中的四个角的元素。 行索引是 [0,0] 和 [3,3]，而列索引是 [0,2] 和 [0,2]
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')
rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)
# 实例3 借助切片 : 或 … 与索引数组组合
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = a[1:3, 1:3]
c = a[1:3, [1, 2]]
d = a[..., 1:]
print(b)
print(c)
print(d)
# 实例4 布尔索引
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
print('\n')

print('大于 5 的元素是：')  # 现在我们会打印出大于 5 的元素
print(x[x > 5])
# 实例5 使用了 ~（取补运算符）来过滤 NaN。
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])
# 实例6 如何从数组中过滤掉非复数元素
a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(a[np.iscomplex(a)])
# 实例7 花式索引  #传入顺序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[4, 2, 1, 7]])
# 实例8 花式索引  传入倒序索引数组
x = np.arange(32).reshape((8, 4))
print(x[[-4, -2, -1, -7]])
# 实例9 传入多个索引数组（要使用np.ix_）
x = np.arange(32).reshape((8, 4))
print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])
# endregion

# region 9、广播(Broadcast)
# 广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 对数组的算术运算通常在相应的元素上进行。
# 如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
# 广播的规则:
# 让所有输入数组都向其中形状最长的数组看齐，形状中不足的部分都通过在前面加 1 补齐。
# 输出数组的形状是输入数组形状的各个维度上的最大值。
# 如果输入数组的某个维度和输出数组的对应维度的长度相同或者其长度为 1 时，这个数组能够用来计算，否则出错。
# 当输入数组的某个维度的长度为 1 时，沿着此维度运算时都用此维度上的第一组值。
# 简单理解：对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足：

# 数组拥有相同形状。
# 当前维度的值相等。
# 当前维度的值有一个是 1。
# 若条件不满足，抛出 "ValueError: frames are not aligned" 异常。
# 实例1：
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])
c = a * b
print(c)
# 实例2： 当运算中的 2 个数组的形状不同时，numpy 将自动触发广播机制
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([1, 2, 3])
print(a + b)
# 实例3： 4x3 的二维数组与长为 3 的一维数组相加，等效于把数组 b 在二维上重复 4 次再运算：
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([1, 2, 3])
bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
print(a + bb)
# endregion

# region 10、迭代数组
# 实例1：
a = np.arange(6).reshape(2, 3)
print('原始数组是：')
print(a)
print('\n')
print('迭代输出元素：')
for x in np.nditer(a):
    print(x, end=", ")
print('\n')
# 实例2：
a = np.arange(6).reshape(2, 3)
for x in np.nditer(a.T):
    print(x, end=", ")
print('\n')

for x in np.nditer(a.T.copy(order='C')):
    print(x, end=", ")
print('\n')
# 实例3：控制遍历顺序 F：列序  C：行序
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('原始数组的转置是：')
b = a.T
print(b)
print('\n')
print('以 C 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=", ")
print('\n')
print('以 F 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=", ")
# 实例4：通过显式设置，来强制 nditer 对象使用某种顺序：
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('以 C 风格顺序排序：')
for x in np.nditer(a, order='C'):
    print(x, end=", ")
print('\n')
print('以 F 风格顺序排序：')
for x in np.nditer(a, order='F'):
    print(x, end=", ")
# 实例5：修改数组中元素的值
# nditer 对象有另一个可选参数 op_flags。 默认情况下，nditer 将视待迭代遍历的数组为只读对象（read-only），为了在遍历数组的同时，实现对数组元素值得修改，必须指定 read-write 或者 write-only 的模式。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = 2 * x
print('修改后的数组是：')
print(a)
# 实例6：使用外部循环
# 参数	描述
# c_index	可以跟踪 C 顺序的索引
# f_index	可以跟踪 Fortran 顺序的索引
# multi_index	每次迭代可以跟踪一种索引类型
# external_loop	给出的值是具有多个值的一维数组，而不是零维数组
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n')
print('修改后的数组是：')
for x in np.nditer(a, flags=['external_loop'], order='F'):
    print(x, end=", ")
# 实例7：广播迭代
# 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。 假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）。
a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('第一个数组为：')
print(a)
print('\n')
print('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('\n')
print('修改后的数组为：')
for x, y in np.nditer([a, b]):
    print("%d:%d" % (x, y), end=", ")

# endregion

# region 11、数组操作
# Numpy 数组操作
# reshape	不改变数据的条件下修改形状
# flat	数组元素迭代器
# flatten	返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
# ravel	返回展开数组
# 实例1：numpy.reshape
a = np.arange(8)
print('原始数组：')
print(a)
print('\n')
b = a.reshape(4, 2)
print('修改后的数组：')
print(b)
# 实例2：numpy.ndarray.flat 是一个数组元素迭代器
a = np.arange(9).reshape(3, 3)
print('原始数组：')
for row in a:
    print(row)
# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
print('迭代后的数组：')
for element in a.flat:
    print(element)
# 实例3：numpy.ndarray.flatten 返回一份数组拷贝，对拷贝所做的修改不会影响原始数组
a = np.arange(8).reshape(2, 4)
print('原数组：')
print(a)
print('\n')
# 默认按行
print('展开的数组：')
print(a.flatten())
print('\n')
print('以 F 风格顺序展开的数组：')
print(a.flatten(order='F'))
# 实例4：numpy.ravel 展平的数组元素，顺序通常是"C风格"，返回的是数组视图（view，有点类似 C/C++引用reference的意味），修改会影响原始数组。
a = np.arange(8).reshape(2, 4)

print('原数组：')
print(a)
print('\n')

print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')

print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))
# 实例5：翻转数组  numpy.transpose
# 函数	描述
# transpose	对换数组的维度
# ndarray.T	和 self.transpose() 相同
# rollaxis	向后滚动指定的轴
# swapaxes	对换数组的两个轴
a = np.arange(12).reshape(3, 4)
print('原数组：')
print(a)
print('\n')
print('对换数组：')
print(np.transpose(a))
print(a.T)
# 实例6：翻转数组 numpy.ndarray.T
a = np.arange(12).reshape(3, 4)
print('原数组：')
print(a)
print('\n')
print('转置数组：')
print(a.T)
# 实例7：numpy.rollaxis 函数向后滚动特定的轴到一个特定位置
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)
print('原数组：')
print(a)
print('获取数组中一个值：')
print(np.where(a == 6))
print(a[1, 1, 0])  # 为 6
print('\n')

# 将轴 2 滚动到轴 0（宽度到深度）
print('调用 rollaxis 函数：')
b = np.rollaxis(a, 2, 0)
print(b)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [0, 1, 1]
# 最后一个 0 移动到最前面
print(np.where(b == 6))
print('\n')
# 将轴 2 滚动到轴 1：（宽度到高度）
print('调用 rollaxis 函数：')
c = np.rollaxis(a, 2, 1)
print(c)
# 查看元素 a[1,1,0]，即 6 的坐标，变成 [1, 0, 1]
# 最后的 0 和 它前面的 1 对换位置
print(np.where(c == 6))
print('\n')
# 实例8：numpy.swapaxes 函数用于交换数组的两个轴
# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)
print('原数组：')
print(a)
print('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）
print('调用 swapaxes 函数后的数组：')
print(np.swapaxes(a, 2, 0))
# 实例9：修改数组维度
x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])
# 对 y 广播 x
b = np.broadcast(x, y)
# 它拥有 iterator 属性，基于自身组件的迭代器元组
print('对 y 广播 x：')
r, c = b.iters
# Python3.x 为 next(context) ，Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))
print('\n')
# shape 属性返回广播对象的形状
print('广播对象的形状：')
print(b.shape)
print('\n')
# 手动使用 broadcast 将 x 与 y 相加
b = np.broadcast(x, y)
c = np.empty(b.shape)
print('手动使用 broadcast 将 x 与 y 相加：')
print(c.shape)
print('\n')
c.flat = [u + v for (u, v) in b]
print('调用 flat 函数：')
print(c)
print('\n')
# 获得了和 NumPy 内建的广播支持相同的结果
print('x 与 y 的和：')
print(x + y)
# 实例10：numpy.broadcast_to 函数将数组广播到新形状。它在原始数组上返回只读视图。 它通常不连续。 如果新形状不符合 NumPy 的广播规则，该函数可能会抛出ValueError。
a = np.arange(4).reshape(1, 4)
print('原数组：')
print(a)
print('\n')
print('调用 broadcast_to 函数之后：')
print(np.broadcast_to(a, (4, 4)))
# 实例11：numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状
x = np.array(([1, 2], [3, 4]))
print('数组 x：')
print(x)
print('\n')
y = np.expand_dims(x, axis=0)
print('数组 y：')
print(y)
print('\n')
print('数组 x 和 y 的形状：')
print(x.shape, y.shape)
print('\n')
# 在位置 1 插入轴
y = np.expand_dims(x, axis=1)
print('在位置 1 插入轴之后的数组 y：')
print(y)
print('\n')
print('x.ndim 和 y.ndim：')
print(x.ndim, y.ndim)
print('\n')
print('x.shape 和 y.shape：')
print(x.shape, y.shape)
# 实例12：numpy.squeeze 函数从给定数组的形状中删除一维的条目
x = np.arange(9).reshape(1, 3, 3)
print('数组 x：')
print(x)
print('\n')
y = np.squeeze(x)
print('数组 y：')
print(y)
print('\n')
print('数组 x 和 y 的形状：')
print(x.shape, y.shape)
# 实例13：连接数组 np.concatenate
# 函数	描述
# concatenate	连接沿现有轴的数组序列
# stack	沿着新的轴加入一系列数组。
# hstack	水平堆叠序列中的数组（列方向）
# vstack	竖直堆叠序列中的数组（行方向）
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')
# 两个数组的维度相同
print('沿轴 0 连接两个数组：')
print(np.concatenate((a, b)))
print('\n')
print('沿轴 1 连接两个数组：')
print(np.concatenate((a, b), axis=1))
# 实例14：连接数组 numpy.stack 函数用于沿新轴连接数组序列
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')
print('沿轴 0 堆叠两个数组：')
print(np.stack((a, b), 0))
print('\n')
print('沿轴 1 堆叠两个数组：')
print(np.stack((a, b), 1))
# 实例15：连接数组 numpy.hstack 是 numpy.stack 函数的变体，它通过水平堆叠来生成数组
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')
print('水平堆叠：')
c = np.hstack((a, b))
print(c)
print('\n')
# 实例16：numpy.vstack 是 numpy.stack 函数的变体，它通过垂直堆叠来生成数组
a = np.array([[1, 2], [3, 4]])
print('第一个数组：')
print(a)
print('\n')
b = np.array([[5, 6], [7, 8]])
print('第二个数组：')
print(b)
print('\n')
print('竖直堆叠：')
c = np.vstack((a, b))
print(c)
# 实例17：分割数组 numpy.split
# 函数	数组及操作
# split	将一个数组分割为多个子数组
# hsplit	将一个数组水平分割为多个子数组（按列）
# vsplit	将一个数组垂直分割为多个子数组（按行）
a = np.arange(9)
print('第一个数组：')
print(a)
print('\n')
print('将数组分为三个大小相等的子数组：')
b = np.split(a, 3)
print(b)
print('\n')
print('将数组在一维数组中表明的位置分割：')
b = np.split(a, [4, 7])
print(b)
# 实例18：分割数组 numpy.split； axis 为 0 时在水平方向分割，axis 为 1 时在垂直方向分割：
a = np.arange(16).reshape(4, 4)
print('第一个数组：')
print(a)
print('\n')
print('默认分割（0轴）：')
b = np.split(a, 2)
print(b)
print('\n')
print('沿水平方向分割：')
c = np.split(a, 2, 1)
print(c)
print('\n')
print('沿水平方向分割：')
d = np.hsplit(a, 2)
print(d)
# 实例19：numpy.hsplit 函数用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组。
harr = np.floor(10 * np.random.random((2, 6)))
print('原array：')
print(harr)
print('拆分后：')
print(np.hsplit(harr, 3))
# 实例20：numpy.vsplit 沿着垂直轴分割，其分割方式与hsplit用法相同。
a = np.arange(16).reshape(4, 4)
print('第一个数组：')
print(a)
print('\n')
print('竖直分割：')
b = np.vsplit(a, 2)
print(b)
# 实例21：数组元素的添加与删除  numpy.resize
# 函数	元素及描述
# resize	返回指定形状的新数组
# append	将值添加到数组末尾
# insert	沿指定轴将值插入到指定下标之前
# delete	删掉某个轴的子数组，并返回删除后的新数组
# unique	查找数组内的唯一元素
a = np.array([[1, 2, 3], [4, 5, 6]])
print('第一个数组：')
print(a)
print('\n')
print('第一个数组的形状：')
print(a.shape)
print('\n')
b = np.resize(a, (3, 2))
print('第二个数组：')
print(b)
print('\n')
print('第二个数组的形状：')
print(b.shape)
print('\n')
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
print('修改第二个数组的大小：')
b = np.resize(a, (3, 3))
print(b)
# 实例22：数组元素的添加与删除  numpy.append 函数在数组的末尾添加值。 追加操作会分配整个数组，并把原来的数组复制到新数组中
a = np.array([[1, 2, 3], [4, 5, 6]])
print('第一个数组：')
print(a)
print('\n')
print('向数组添加元素：')
print(np.append(a, [7, 8, 9]))
print('\n')
print('沿轴 0 添加元素：')
print(np.append(a, [[7, 8, 9]], axis=0))
print('\n')
print('沿轴 1 添加元素：')
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))
# 实例23：数组元素的添加与删除  numpy.insert 函数在给定索引之前，沿给定轴在输入数组中插入值
a = np.array([[1, 2], [3, 4], [5, 6]])
print('第一个数组：')
print(a)
print('\n')
print('未传递 Axis 参数。 在删除之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print('\n')
print('传递了 Axis 参数。 会广播值数组来配输入数组。')
print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print('\n')
print('沿轴 1 广播：')
print(np.insert(a, 1, 11, axis=1))
# 实例24：数组元素的添加与删除  numpy.delete 函数返回从输入数组中删除指定子数组的新数组。 与 insert() 函数的情况一样，如果未提供轴参数，则输入数组将展开
a = np.arange(12).reshape(3, 4)
print('第一个数组：')
print(a)
print('\n')
print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('\n')
print('删除第二列：')
print(np.delete(a, 1, axis=1))
print('\n')
print('包含从数组中删除的替代值的切片：')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))
# 实例25：数组元素的添加与删除  numpy.unique 函数用于去除数组中的重复元素
a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print('第一个数组：')
print(a)
print('\n')
print('第一个数组的去重值：')
u = np.unique(a)
print(u)
print('\n')
print('去重数组的索引数组：')
u, indices = np.unique(a, return_index=True)
print(indices)
print('\n')
print('我们可以看到每个和原数组下标对应的数值：')
print(a)
print('\n')
print('去重数组的下标：')
u, indices = np.unique(a, return_inverse=True)
print(u)
print('\n')
print('下标为：')
print(indices)
print('\n')
print('使用下标重构原数组：')
print(u[indices])
print('\n')
print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)
# endregion

# region 12、字符串函数
# add()	对两个数组的逐个字符串元素进行连接
# multiply()	返回按元素多重连接后的字符串
# center()	居中字符串
# capitalize()	将字符串第一个字母转换为大写
# title()	将字符串的每个单词的第一个字母转换为大写
# lower()	数组元素转换为小写
# upper()	数组元素转换为大写
# split()	指定分隔符对字符串进行分割，并返回数组列表
# splitlines()	返回元素中的行列表，以换行符分割
# strip()	移除元素开头或者结尾处的特定字符
# join()	通过指定分隔符来连接数组中的元素
# replace()	使用新字符串替换字符串中的所有子字符串
# decode()	数组元素依次调用str.decode
# encode()	数组元素依次调用str.encode
# 实例1：numpy.char.add() 函数依次对两个数组的元素进行字符串连接
print('连接两个字符串：')
print(np.char.add(['hello'], [' xyz']))
print('\n')
print('连接示例：')
print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))
# 实例2：numpy.char.multiply() 函数执行多重连接
print(np.char.multiply('Runoob ', 3))
# 实例3：numpy.char.center() 函数用于将字符串居中，并使用指定字符在左侧和右侧进行填充
# np.char.center(str , width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('Runoob', 20, fillchar='*'))
# 实例4：numpy.char.capitalize() 函数将字符串的第一个字母转换为大写
print(np.char.capitalize('runoob'))
# 实例5：numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写
print(np.char.title('i like runoob'))
# 实例6：numpy.char.lower() 函数对数组的每个元素转换为小写。它对每个元素调用 str.lower
print(np.char.lower(['RUNOOB', 'GOOGLE']))  # 操作数组
# 操作字符串
print(np.char.lower('RUNOOB'))  # 操作数组
# 实例7：numpy.char.upper() 函数对数组的每个元素转换为大写。它对每个元素调用 str.upper
print(np.char.upper(['runoob', 'google']))  # 操作数组
print(np.char.upper('runoob'))  # 操作字符串
# 实例8：numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格
print(np.char.split('i like runoob?'))  # 分隔符默认为空格
print(np.char.split('www.runoob.com', sep='.'))  # 分隔符为 .
# 实例9：numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组
print(np.char.splitlines('i\nlike runoob?'))  # 换行符 \n
print(np.char.splitlines('i\rlike runoob?'))  # 换行符 \r
# 实例10：numpy.char.strip() 函数用于移除开头或结尾处的特定字符
print(np.char.strip('ashok arunooba', 'a'))  # 移除字符串头尾的 a 字符
print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))  # 移除数组元素头尾的 a 字符
# 实例11：numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
print(np.char.join(':', 'runoob'))  # 操作字符串
print(np.char.join([':', '-'], ['runoob', 'google']))  # 指定多个分隔符操作数组元素
# 实例12：numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串
print(np.char.replace('i like runoob', 'oo', 'cc'))
# 实例13：numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器
a = np.char.encode('runoob', 'cp500')
print(a)
# 实例14：numpy.char.decode() 函数对编码的元素进行 str.decode() 解码
a = np.char.encode('runoob', 'cp500')
print(a)
print(np.char.decode(a, 'cp500'))
# endregion

# region 13、数学函数
# 实例1：NumPy 提供了标准的三角函数：sin()、cos()、tan()。
a = np.array([0, 30, 45, 60, 90])
print('不同角度的正弦值：')
# 通过乘 pi/180 转化为弧度
print(np.sin(a * np.pi / 180))
print('\n')
print('数组中角度的余弦值：')
print(np.cos(a * np.pi / 180))
print('\n')
print('数组中角度的正切值：')
print(np.tan(a * np.pi / 180))
# 实例2：arcsin，arccos，和 arctan 函数返回给定角度的 sin，cos 和 tan 的反三角函数
a = np.array([0, 30, 45, 60, 90])
print('含有正弦值的数组：')
sin = np.sin(a * np.pi / 180)
print(sin)
print('\n')
print('计算角度的反正弦，返回值以弧度为单位：')
inv = np.arcsin(sin)
print(inv)
print('\n')
print('通过转化为角度制来检查结果：')
print(np.degrees(inv))
print('\n')
print('arccos 和 arctan 函数行为类似：')
cos = np.cos(a * np.pi / 180)
print(cos)
print('\n')
print('反余弦：')
inv = np.arccos(cos)
print(inv)
print('\n')
print('角度制单位：')
print(np.degrees(inv))
print('\n')
print('tan 函数：')
tan = np.tan(a * np.pi / 180)
print(tan)
print('\n')
print('反正切：')
inv = np.arctan(tan)
print(inv)
print('\n')
print('角度制单位：')
print(np.degrees(inv))
# 实例3：舍入函数 numpy.around() 函数返回指定数字的四舍五入值
a = np.array([1.0, 5.55, 123, 0.567, 25.532])
print('原数组：')
print(a)
print('\n')
print('舍入后：')
print(np.around(a))
print(np.around(a, decimals=1))
print(np.around(a, decimals=-1))
# 实例4：numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print('提供的数组：')
print(a)
print('\n')
print('修改后的数组：')
print(np.floor(a))
# 实例5：numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整
a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
print('提供的数组：')
print(a)
print('\n')
print('修改后的数组：')
print(np.ceil(a))
# endregion

# region 14、算术函数
# NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
a = np.arange(9, dtype=np.float_).reshape(3, 3)
print('第一个数组：')
print(a)
print('\n')
print('第二个数组：')
b = np.array([10, 10, 10])
print(b)
print('\n')
print('两个数组相加：')
print(np.add(a, b))
print('\n')
print('两个数组相减：')
print(np.subtract(a, b))
print('\n')
print('两个数组相乘：')
print(np.multiply(a, b))
print('\n')
print('两个数组相除：')
print(np.divide(a, b))

# 实例2：numpy.reciprocal() 函数返回参数逐元素的倒数
a = np.array([0.25, 1.33, 1, 100])
print('我们的数组是：')
print(a)
print('\n')
print('调用 reciprocal 函数：')
print(np.reciprocal(a))
# 实例3：numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂
a = np.array([10, 100, 1000])
print('我们的数组是；')
print(a)
print('\n')
print('调用 power 函数：')
print(np.power(a, 2))
print('\n')
print('第二个数组：')
b = np.array([1, 2, 3])
print(b)
print('\n')
print('再次调用 power 函数：')
print(np.power(a, b))
# 实例4：numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果
a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
print('第一个数组：')
print(a)
print('\n')
print('第二个数组：')
print(b)
print('\n')
print('调用 mod() 函数：')
print(np.mod(a, b))
print('\n')
print('调用 remainder() 函数：')
print(np.remainder(a, b))
# endregion
