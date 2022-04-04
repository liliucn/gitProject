# region 1、特殊符号
# #  \ 表示续行符
# #  \t 制表符
# # \n 换行符
# endregion

# region 2、input

#region 2.1 数据类型
b = str(123)
c = int('123233')
d = float('1.23')
print(b)
print(c)
print(d)
a=input('请输入你的年龄')
b=input('请输入你的姓名')
print("my name is %s, my age is%d"%(b,int(a)))

#字符串反转
name='basdfwe武'
print(name[len(name):1:-1])
#endregion

#region 2.2 格式化输出
print('我的名字是:%s,我今年%d岁,体重是%f公斤'%('武月',19,50)) #没保留小数 按顺序来放到相应位置
a=input("请输入你的年龄：")
print("你明年，是{0}岁".format(int(a)+1))
b=input("请输入你的年龄：")
print("你明年，是%d岁"%(int(b)+1))
print("你明年，是%s岁"%str(int(b)+1))
#endregion

#region 2.3 格式化字符串 用%代替
a='abcdeefg'
print(a[1:3])
b=3
c='有'
print("asd%d%s"%(b,c))
print("格式化数字：%d"%b)
print("格式化字符串%s"%c)
#endregion

#region 2.4 格式化字符串 用str.format
name='world'
print("hello {0}".format(name))
age=20
weight=45.34
print("我的名字叫{2},我今年{0}岁,我{1}公斤".format(age,weight,name))
print("我的名字叫%s,我今年%d岁,我%.2f公斤"%(name,age,weight)) #保留了2位小数
#endregion

#region 2.5 日期格式化补0
from datetime import date,datetime
print("%5s" % '2')
print("%-5s" % '2')
print(str(datetime.now().year)+'-'+('%02d'%int(datetime.now().month))+'-'+('%02d'%int(datetime.now().day))+' '+
      ('%02d'%int(datetime.now().hour))+'-'+('%02d'%int(datetime.now().minute))+'-'+('%02d'%int(datetime.now().second)))
#endregion

#region 2.6 元组操作
tuple1=(4,2,6,10,9,8)
num=len(tuple1)
print('长度：'+str(num))

tuple1=(4,2,6,10,9,8)
num=max(tuple1)
print('最大值：'+str(num))

tuple1=(4,2,6,10,9,8)
num=min(tuple1)
print('最小值'+str(num))

students=['jack','tom','john','amy','kim','sunny']
print(students)
tuple1=tuple(students)
print(tuple1)
#endregion

#region 2.7 字符串函数
name='basdfwe李'
print(name[len(name):1:-1])

str1 = 'hello world'
print(str1.count('or',0,))
print(str1.index('l'))
print(str1[str1.find('o')+1:])
print(str1.count('o',0,))

str1= 'hello world hello china'
print(str1.replace('hello','HELLO'))
print(str1.replace('hello','HELLO'))

str1 = 'hello world hello china'
print(str1.split(' '))
print(str1.split(' ',2))
# 1.计算字符串'i love python'中子串o出现的次数.
# 2.从键盘输入一个字符串，将小写字母全部转换成大写字母
str1 = 'hello world hello china'
print(str1.capitalize())
print(str1.title())
str1 = 'hello world hello china'
print(str1.startswith('hello')) #是否以hello开头 返回True 或 False
print(str1.endswith('china')) #是否以china结尾 返回True 或 False

str1 = 'Hello World HELLO CHINA'
print(str1.lower())
str1 = 'hello world hello china'
print(str1.upper())
str1 = 'hello'
print(str1.ljust(10))
str1 = 'hello'
print(str1.rjust(10))
str1 = 'hello'
print(str1.center(15))
str1 = '     hello'
print(str1)
print(str1.lstrip())
str1 = 'hello     '
print(str1)
print(str1.rstrip())
str1 = '     hello     '
print(str1)
print(str1.strip ())
str1 = 'hello world hello china'
print(str1.partition('world'))
str1='_'
list = ['hello','world','hello','china']
print(str1.join(list))
str1 = ' '
print(str1.isspace())
str1='a123@'
print(str1.isalnum())
str1='123'
print(str1.isdigit())
str1='aaa'
print(str1.isalpha())
#endregion

# region 2.8 end print结尾默认有一个换行符；加一个end='' 就是将换行符去掉
# a = "python"
# list1 = ['hello', 'world', 'china', 'english']
# print (''.join (list1))
# for i in list1:
#     print (i, end=(';'))
#endregion

#region 2.9 练习
# 1.计算字符串'i love python'中子串o出现的次数.
# 2.从键盘输入一个字符串，将小写字母全部转换成大写字母
a=['e',1,'abc',2,'23']
b=[1,2,1,20,3,5,6]
b.sort();
print(b)
a.append('python')
a.insert(3,'sa')
print("a数据集:"+str(a))
b=a.insert(3,'sa')
b=a.copy();
print("b数据集:"+str(b))

a = '123456789'
b = a[1:5:-1]
a = [1, 23, '武月', 'li']
print(a)
print(a[-1])
a.append("abc")
print(a)
# endregion
# endregion

#region 3、sorted 函数 算法
ss=['ab','cde','f','ghil']
sT=sorted(ss,key=lambda x:len(x)) #升序
sT=sorted(ss,key=lambda x:len(x),reverse=True) #降序
print(sT)
#endregion

#region 4、选择排序
# def selection_sort(arr):
#     """选择排序"""
#     # 第一层for表示循环选择的遍数
#     for i in range(len(arr) - 1):
#         # 将起始元素设为最小元素
#         min_index = i
#         # 第二层for表示最小元素和后面的元素逐个比较
#         for j in range(i + 1, len(arr)):
#             if arr[j] < arr[min_index]:
#                 # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
#                 min_index = j
#         # 查找一遍后将最小元素与起始元素互换
#         arr[min_index], arr[i] = arr[i], arr[min_index]
#     return arr
# selection_sort([89, 29, 39 , 19, 97, 88, 77, 11, 11, 22,33, 63, 44, 22])


#endregion

#region 5、选择排序输出菱形
# total = 6
# row = 1
# while row <= 6:
#     col = 1     # 保证每次内循环col都从1开始，打印前面空格的个数
#     while col <= (6-row):  # 这个内层while就是单纯打印空格
#         print(' ', end='')  # 空格的打印不换行
#         col += 1
#     print(row * '* ')  # 每一行打印完空格后，接着在同一行打印星星，星星个数与行数相等，且打印完星星后print默认换行
#     row += 1
#
# bottom = 6
# while bottom > 0:
#     col = 1     # 保证每次内循环col都从1开始，打印前面空格的个数
#     while bottom+col <= 6:
#         print(' ', end='')  # 空格的打印不换行
#         col += 1
#     print(bottom * '* ')  # 每一行打印完空格后，接着在同一行打印星星，星星个数与行数相等，且打印完星星后print默认换行
#     bottom -= 1

#endregion

#region 6、选择排序输出菱形每3步踢除一个人
# a=list(range(1,18))
# for i in a:
#     c = len(a) % 3
#     b = []
#     if c == 0: #输入的数字能整除3
#         for i in range(1, len(a) + 1):
#             if i % 3 != 0:
#                 b.append(a[i - 1])
#         a = b
#     else:#不能整除3的
#         for i in range(1, len(a) + 1):
#             if i % 3 != 0:
#                 b.append(a[i - 1])
#         a = b[-c:] + b[:-c]
#     print(a)
#     if len(a)==2:
#         break;
# print("最后一个人序号为：{}".format(a[1]))
#endregion

# region 7、循环
list1=[1,2,'helloworld',3,12]
for i in list1:
    print(i)
i=0
while i<len(list1):
    print(list1[i])
    i=i+1;

a=[]
x = int(input("请输入第一个最大值: "))
y = int(input("请输入第二个最大值: "))
z = int(input("请输入第三个最大值: "))
a.append(x)
a.append(y)
a.append(z)
print(a)
maxNum=0;
for i in a:
    if maxNum<i:
        maxNum=i;
print(maxNum)
# endregion

# region 8、字典遍历循环
dic={"1":{"ID":"1","Name":"lisi","age":"34"},
     "2":{"ID":"2","Name":"wangwu","age":"26"},
    "3": {"ID":"3","Name":"qianba","age":""}}
nameKey="Name"
nameValue="qianba"
for i in dic.keys():
    for j in dic[i].keys():
        if str(j)==str(nameKey)and dic[i][j]==nameValue: # 只输出qianba的年龄
            if str(j)==str(nameKey): #输出所有人的年龄，如果年龄是空值则输出18
                if(str(dic[i]["age"])==''):
                    print((dic[i][j])+"年龄：18")
                else :
                    print((dic[i][j])+"年龄："+str(dic[i]["age"]))
# endregion

#region 9、函数
#region 9.1、带参参数
def say_hi(a,b):
    print("你好{0},你好工{0},我叫{1}".format(a,b))

say_hi("张三","李四")
def f(a,b,c):
    if c=="+":
        print (a+b)
    elif c=="-":
        print (a-b)
    elif c=="/":
        print(a/b)
    elif c=="*":
        print(a*b)
f(12,6,"*")
#endregion

# region 9.2、可变参数 不可变参数 * 表示 元组
# # *  一颗星  表示 元组
def say(a,b=1,*c):  # b 默认值为1
    print(a,b,c)
say(1,2,3,4,"python","helloworld")

#** 两颗星 表示  字典
def say2(a,b,**c):
    print(a,b,c)
say2(1,2,name="python",k="helloworld")

# * 和 ** ，一颗星和两颗星联用
def say3(a,*b,**c):
    print(a,b,c)
say3(1,2,4,5,6,name="python",k="helloworld")
# endregion

# region 9.3、匿名函数 lambda函数
# lambda 无参函数
f=lambda :"小明"
print(f())

# lambda 有参函数  两个参数
c = lambda e, d: e*10 + d
print(c(10,3))

# lambda 有参函数 一个参数x 函数体是 x=x*x   d1 和d2 是一样的；d1是有参的lambda函数
d2=lambda x:x**2;
print(d2(10))

def d1(x):
    print(x*x)
d1(10)

# 匿名函数
a=[i for i in range(1,100)]
print(a)
b=[j for j in range(1,100) if j%3==0]
print (b)
# lambda 和 匿名函数合用
c=lambda b:[j for j in range(1,b+1) if j%3==0]
print (c(50))
# endregion

# region 9.4、高阶函数 Filter(),map(),reduce()
# region 9.4.1、filter函数  【返回的是列表list】
def f(n):
    if n >= 0:
        return True;
    else:
        return False;
foo = [2, 18, 9, -22, -17, -24, 8, 12, 27]
r = filter (f, foo)
print (list (r));

# 过滤 小数点后面不为0的数
s=[6872.24,345.23,78.0,79.]
a=filter(lambda x:str(x).split('.')[1]=='0',s)
print(list(a))

# region  filter 过滤 现在有一个列表，里面存储一些日期数据格式是 '2018-11-11',要求将这个列表中所有2018年7-8月份1-15号的日期数据提取出来
#第一种 循环
t = ['2016-5-12', '2016-7-15', '2016-11-11', '2016-8-11', '2016-7-11', '2018-5-12', '2018-7-15', '2018-11-11',
     '2018-8-11', '2018-7-11']
for i in t:
    j = i.split ('-');
    if (j[0] == "2018" and (j[1] == "7" or j[1] == "8") and (int (j[2]) >= 1 and int (j[2]) <= 15)):
        print (i);

# 第二种 filter
def t_clean(x):
    year = int (x.split ('-')[0])
    month = int (x.split ('-')[1])
    day = int (x.split ('-')[2])
    if year == 2018 and (month == 7 or month == 8) and (1 <= day <= 15):
        return True
    else:
        return False

result = filter (t_clean, t)
print (list (result))
# endregion
# endregion

# region 9.4.2、map函数 方式一和方式二是等价的  【返回的是列表list】
#方式一
l = [i for i in range (1, 10)]
print (l)
f = lambda x: x**2;
r = map (f, l)
print (list (r))
#方式二
print(list(map(lambda x:x**2,[i for i in range(1,10)])))

#例子
#1. 对[1, 2, 3, 4, 5]中的每个元素进行平方运算：
print(list(map(lambda a:a**2,[1, 2, 3, 4, 5])))
#2对[1, 3, 5, 7, 9], [2, 4, 6, 8, 10] 两个序列中的元素依次求和
print(list(map(lambda b,c:b+c,[1, 3, 5, 7, 9], [2, 4, 6, 8, 10] )))
# endregion

# region 9.4.3、reduce函数
import functools
l=[[1,2,2,3,4,5],[1,2,3,4]]
ll=[1,2,2,3,4,5]
b=functools.reduce(lambda x,y:x+y,ll)
print(b)

## 输出1!+2!+3!+4!+5! -->153
f = lambda n: f (n - 1)*n if n >= 2 else 1
m = map (lambda n: functools.reduce (lambda x, y: x*y, range (1, n + 1)), range (1, 6))
print (list (m)) #此行不注释，下一行报错；map执行了，就释放了，所以下面的m为空
result=functools.reduce (lambda x, y: x + y, list(m))
print(result)
# endregion
# endregion

#region 9.5、高阶函数 练习
names=['leo','susan','herry','black']
ages=[11,22,33,44]
sex=['man','woman','man','man']
# 第一步：格式化用户的英文名，要求首字母大小，其它字母小写
one=list(map(lambda x:x.title(),names))
# 第二步：将用户英文名、年龄、性别三个数据结合到一起，形成一个新数据
two=list(map(lambda x,y,z:[x,str(y),z],one,ages,sex))
# 第三步：过滤性别为男的用户
three=list(filter(lambda x: x[2]=='man',two))
# 第四步：取每个元素的中的年龄[list]
four=list(map(lambda t:t[1],three))
# 第五步：求性别为男的用户的平均年龄
import functools
five=(functools.reduce(lambda x,y:(int(x)+int(y)),four))/len(four)

# 3.编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n
import functools
def f():
    n = input ("请输入一个数：")
    if n.isdigit ():
        if int (n)%2 == 0:
            return functools.reduce (lambda x, y: 1/x + 1/y, range (2, int (n) + 1, 2))
        else:
            return functools.reduce (lambda x, y: 1/x + 1/y, range (1, int (n) + 1, 2))
a = f ()
print (a)
#endregion
#endregion

# region 10、可变对象 不可变对象
# 不可变对象，改变函数外面的变量
x = 1
def func():
    x = 2
func()
print(x)

# 可变对象，改变函数外面的变量
x = 1
def func():
    global x
    x = 2
func()
print(x)
# endregion

# region 11、递归 阶乘
# # 方式1，递归
f = lambda n: f(n-1) * n if n>=2 else 1
print(f(5))

# 方式2 reduce
from functools import reduce
f_5=reduce(lambda x,y:x*y,range(1,6))
print(f_5)

# 方式3，递归
def f(n):
    if n == 1:
        return 1;
    else:
        return n*f (n - 1)
print (f (5))
# endregion

# region 12、斐波那契数列   1 1 2 3 5 8 13
def f(n):
    if n==1 or n==2:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(7))

y=lambda x : 1 if x==1 or x==2 else y(x-1)+y(x-2)
print(y(7))
# endregion

# region 13、迭代器
l = iter([1, 2, 3, 4, 5])
for i in l:
    print(i)
print ('$'*50)
#endregion

#region 14、yield 运行到yield程序都会暂停，只有调用next()函数时才会继续执行
def f():
    yield 1
    yield 2
    yield 3
a=f()
print(a)
print(next(a))
print(next(a))
print(next(a))
#endregion

#region 14、yield 直接返回一个list
def m():
    for i in range(10):
        yield i;
a=m();
print(list(a))
# endregion

# region 15、文件读取
# 1.读取
# （1）r      只读，前提：文件必须存在
# （2）r+   读写，前提：文件必须存在
# 2.写（重新开始写，把原来的内容抹掉）
# （1）w     只写，文件可以不存在，会自动建立
# （2）w+   读写，文件可以不存在，会自动建立
# 3.追加（在原内容的后面写入新的内容）
# a
# 4.二进制形式（图像，音频，视频）
# b

# 文件读取
f = open ("1234.txt","r", encoding="utf-8")
print(f.read())
print(f.readline()) #读取第一行
print(f.readlines()) #读取所有行
# 文件写入
f = open ("1234.txt", "a", encoding="utf-8")
print (f.write ("aaaaa"))  # 覆盖写入
# endregion

#region 16、导入random模块
import random as rd;
import numpy as np

for i in range (1, 10):
    print (rd.randint (1, 100))
red=np.random.randint(1,33)
a=np.random.choice(red,6)
print(a)

bleen=np.random.randint(1,16)
print(bleen)

red=rd.sample(range(1,33),6)
print(red)
bleen=rd.randint(1,16)
print(bleen)

listT=list(range(1,33))
rd.shuffle(listT)
print(listT[0:6])
#endregion

# region 17、导入Time模块
# 1.time.time()：获取当前时间戳。
# 2.time.localtime([secs])：时间戳转时间元组
# 3.time.mktime(t)：时间元组转时间戳。
# 4.time.asctime([t])：时间元组戳转标准时间格式，如'Sun Jun 20 23:21:05 1993'。
# 5.time.strftime(format[, t])：时间元组转自定义时间字符串
# 6.time.strptime(string[, format])：自定义时间字符串转时间元组
import time
print(time.time())
print(time.localtime())
print(time.clock())
print (time.strftime ('%Y-%m-%d', time.localtime ()))
t = time.strptime ('2019-11-11 12:03:44', '%Y-%m-%d %H:%M:%S')
print (time.mktime (t))
# endregion

# region 18、调用数据库 及 增、删、改、查 等操作
#region 18.1 安装pymysql 及 命令说明
# 安装pymysql
# pip install pymysql
# cmd 管理员运行

# 修改pip镜像源
# 1.在windows文件管理器中,输入 %APPDATA% C:\Users\liliu\AppData\Roaming\
# 2.在返回目录下新建pip文件夹，然后到pip文件夹里面去新建个pip.ini文件
# 3.在新建的pip.ini文件中输入以下内容
#endregion

#region 18.2 调用数据库
import pymysql
# pymysql.connect(host,user,passwd,port,db,charset)	链接数据库
# conn.cursor()	操作游标
# cursor.execute(sql,parm)	执行sql语句
# cursor.fetchmany(num)	从结果集中获取指定数目的记录
# cursor.fetchone()	得到结果集一条记录
# cursor.fetchall()	得到结果集所有记录
conn = pymysql.connect(host='localhost',user='root', password='123456',db='test',port=3306,charset='utf8')
cursor=conn.cursor()#创建游标
#在当前链接的数据库里创建表
# createSql="create table if not exists tableTemp(Name varchar(20) not null,ID int)"
# cursor.execute(createSql)
#endregion

#region 18.3、不带参访问数据库 增删改查操作
##新建记录
createSql="INSERT INTO tableTemp VALUES('张三',1),('李四',2)"
cursor.execute(createSql)
# 修改记录
createSql="UPDATE tableTemp SET NAME='了了了' WHERE ID=1"
cursor.execute(createSql)
# 删除记录
createSql="DELETE FROM tableTemp WHERE ID=2"
cursor.execute(createSql)
# 查询数据
createSql="SELECT * FROM tableTemp"
result=cursor.execute(createSql)
cursor.fetchone();
#endregion 不带参访问数据库

#region 18.4、带参访问数据库 增删改查操作 【？？？？不可以传数值吗？？】
tempSql="insert into tableTemp values(%s,%s)"
parm=('李同学','18')
cursor.execute(tempSql,parm)

tempSql="insert into tableTemp values(%(name)s,%(id)s)"
value = {'name':'zhangsan','id':'12'};
cursor.execute(tempSql,value)
#endregion

conn.commit()#向数据库提交操作
cursor.close()#关键游标
conn.close()#关闭链接
#endregion

#region 19、正则表达式
import re
#match 返回match对象，从头开始匹配，当匹配不到信息时返回None
# re.match(pattern,string)
patternTemp='abc'
strTemp='aabcdea'
print(re.search(patternTemp,strTemp))
import re

# \d 匹配一个数字字符。等价于 [0-9]。
# \D 匹配一个非数字字符。等价于 [^0-9]。
# \w 匹配字母、数字、下划线。等价于'[A-Za-z0-9_]'。
# \W 匹配非字母、数字、下划线。等价于 '[^A-Za-z0-9_]'。
# \s 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S 匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# . 匹配除换行符（\n、\r）之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用像"(.|\n)"的模式。 转义加斜线 \.
# \ 将下一个字符标记为一个特殊字符、或一个原义字符、或一个 向后引用、或一个八进制转义符。例如，'n' 匹配字符 "n"。'\n' 匹配一个换行符。序列 '\\' 匹配 "\" 而 "\(" 则匹配 "("。
# ^ 匹配输入字符串的开始位置。如果设置了 RegExp 对象的 Multiline 属性，^ 也匹配 '\n' 或 '\r' 之后的位置。
# $ 匹配输入字符串的结束位置。如果设置了RegExp 对象的 Multiline 属性，$ 也匹配 '\n' 或 '\r' 之前的位置。
# * 匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
# + 匹配前面的子表达式一次或多次。例如，'zo+' 能匹配 "zo" 以及 "zoo"，但不能匹配 "z"。+ 等价于 {1,}。
# ? 匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。
# {n}n 是一个非负整数。匹配确定的 n 次。例如，'o{2}' 不能匹配 "Bob" 中的 'o'，但是能匹配 "food" 中的两个 o。
# {n,}n 是一个非负整数。至少匹配n 次。例如，'o{2,}' 不能匹配 "Bob" 中的 'o'，但能匹配 "foooood" 中的所有 o。'o{1,}' 等价于 'o+'。'o{0,}' 则等价于 'o*'。
# {n,m}m 和 n 均为非负整数，其中n <= m。最少匹配 n 次且最多匹配 m 次。例如，"o{1,3}" 将匹配 "fooooood" 中的前三个 o。'o{0,1}' 等价于 'o?'。请注意在逗号和两个数之间不能有空格。

## 限定符 有* 或 + 或 ？ 或{n} 或 {n,} 或 {n,m} 有6次 如下
## 边界限定字符 ^ 和 $ 分别代表 开始和结束字符

# {n} 固定多少次  result=re.search('\w{6}\s\d\.\d',strTemp)
# {n,}最少要出现n次 result=re.search('\w{1,}\s\d\.\d',strTemp)
# {n,m}最少要出现n次，最多出现m 次 result=re.search('\w{1,6}\s\d\.\d',strTemp)
# ？匹配前面的子表达式零次或一次。例如，"do(es)?" 可以匹配 "do" 或 "does" 。? 等价于 {0,1}。
# *	匹配前面的子表达式零次或多次。例如，zo* 能匹配 "z" 以及 "zoo"。* 等价于{0,}。
# x|y	匹配 x 或 y。例如，'z|food' 能匹配 "z" 或 "food"。'(z|f)ood' 则匹配 "zood" 或 "food"。
# [xyz]	字符集合。匹配所包含的任意一个字符。例如， '[abc]' 可以匹配 "plain" 中的 'a'。
# [^xyz]	负值字符集合。匹配未包含的任意字符。例如， '[^abc]' 可以匹配 "plain" 中的'p'、'l'、'i'、'n'。
# [a-z]	字符范围。匹配指定范围内的任意字符。例如，'[a-z]' 可以匹配 'a' 到 'z' 范围内的任意小写字母字符。
# [^a-z]	负值字符范围。匹配任何不在指定范围内的任意字符。例如，'[^a-z]' 可以匹配任何不在 'a' 到 'z' 范围内的任意字符。


#match 返回match对象，从头开始匹配，当匹配不到信息时返回None ，只会找到第一个匹配到的对象
strT='abcaaaabcaasdfas123df python123asdfb'
partten='abc'
result=re.match(partten,strT)
print(result.group()) #group 返回匹配的内容

#search只会找到第一个匹配到的对象
patternTemp='123'
strTemp='abcaaaabcaasdfas123df python123asdfb'
print(re.search(patternTemp,strTemp).group())

#findall 返回的是列表 ,有括号的话,只返回括号里面的
patternTemp='abc'
strTemp='abcaaaabcaasdfas123df python123asdfb'
print(re.findall(patternTemp,strTemp))

#普通字符搭配使用
string='http://www.baidu.com'
result=re.search('baidu',string)
print(result.group())
#非打印字符
string='\nhttp://www.baidu.com\n\thttp://www.baidu.com\n'
print(string)
result=re.findall('\t',string)
print(result)

# 只提出python
strTemp='abcaaaabcaasdfas123df python 3.5123asdfbabc$'
#只取python,不加括号,用截取的方式去掉前后空格
result=re.search('\s\w{6}\s',strTemp)
print(result.group()[1:])
#只取python,加括号,只取括号里面的内容
result=re.search('\s(\w{6})\s',strTemp)
print(result.group(1))

strTemp='abcaaaabcaasdfas123df python 3.5123asdfbabc$'
result=re.search('\w\w\w\w\w\w\s\d\.\d',strTemp)

result=re.search('\w{6}\s\d\.\d',strTemp)
result=re.search('\w{1,}\s\d\.\d',strTemp)

result=re.search('abc\$',strTemp) #查找结尾位置的abc
result=re.search('^abc',strTemp) #查找开始位置的abc
print(result.group())

string="name:小明age:16,name:小白age:17,name:小黑 age:15"
result=re.findall('name:(.*?)age:(\d{1,})',string) #查找结尾位置的abc
print(list(result))


# 长度11位 开头是1 第2位是35678
string=input('请输入一个电话')
result=re.match('^1[35678]\d{9}',string) #查找结尾位置的abc
if re.match('^1[35678]\d{9}',string):
    print('输入的是一个电话号码')
else :
    print("不是一个电话号码")

#替换
a='语文59分'
print(re.sub('\d+','100',a))

#替换
string='abcdefg 北风网 上海 404 not found'
print(re.search('\s(.*?\s.*?)\s',string)) #查找

# 1：tels=[13100008724,15898030575,13776814997,18915089373,18917210234,20000,342422199802021448]
# # 匹配不是以4和7结尾的手机号 开头1  第二位35678
import re
tels=[13100008724,15898030575,13776814997,18915089373,18917210234,20000,342422199802021448]
partten='^1[35678]\d{8}[01235689]$' #查找结尾位置的abc
for i in tels:
    if re.findall(partten,str(i)):
        print(i)
# 2：.使用正则匹配提取出每个<a里面的所有中文文本信息并且写入到txt文件里


str7='''<div class="s_tab_inner">
    <b>网页</b>
    <a href="//www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'news'})" sync="true">资讯</a>
    <a href="http://tieba.baidu.com/f?kw=&fr=wwwt" wdfield="kw"  onmousedown="return c({'fm':'tab','tab':'tieba'})">贴吧</a>
    <a href="http://zhidao.baidu.com/q?ct=17&pn=0&tn=ikaslist&rn=10&word=&fr=wwwt" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'zhidao'})">知道</a>
    <a href="http://music.taihe.com/search?fr=ps&ie=utf-8&key=" wdfield="key"  onmousedown="return c({'fm':'tab','tab':'music'})">音乐</a>
    <a href="http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'pic'})">图片</a>
    <a href="http://v.baidu.com/v?ct=301989888&rn=20&pn=0&db=0&s=25&ie=utf-8&word=" wdfield="word"   onmousedown="return c({'fm':'tab','tab':'video'})">视频</a>
    <a href="http://map.baidu.com/m?word=&fr=ps01000" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'map'})">地图</a>
    <a href="http://wenku.baidu.com/search?word=&lm=0&od=0&ie=utf-8" wdfield="word"  onmousedown="return c({'fm':'tab','tab':'wenku'})">文库</a>
    <a href="//www.baidu.com/more/"  onmousedown="return c({'fm':'tab','tab':'more'})">更多»</a>'''
result=re.findall('<a.*?>(.*?)</a>',str7) #查找结尾位置的abc

def writeTxt(result):
    with open ("python a text值.txt", "a", encoding="utf-8") as a:
        # a.writelines(result) #不换行
        a.writelines([line+'\n' for line in result]) #换行
writeTxt(result)


#输入一个日期
#日期是年月日格式{yyyy-mm-dd} 或 {yyyy/mm/dd}
import re
def ValidateDay(dayT):
    dayArray=re.split('[-/]', dayT)
    if len(dayArray)==3:
        if len(dayArray[0]) != 4 or int(dayArray[0]) < 1900:
            return "日期格式错误: 年份应为4位数 并且 年份应为1900年以后的年份"
        elif int(dayArray[1]) < 1 or int(dayArray[1]) >12:
            return "日期格式错误: 年份应在 1-12个月之间"
        elif int(dayArray[2]) < 1 or int(dayArray[2]) >31:
            return "日期格式错误: 年份应在 1-31号之间"
    else:
        return "日期格式错误: 日期的年月日应该以 / 或 - 进行分隔"
dayTemp=input('请输入一个日期')
print(ValidateDay(dayTemp))
#endregion

# region 20、urllib 抓取
import urllib.request
urlTemp="http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-24hours-0-0-1-1"
returnTemp = urllib.request.urlopen(urlTemp)
print(returnTemp.read().decode("gbk"))
# endregion

#region request请求
import  requests
temp=requests.get("https://www.jd.com");
print(temp.content) # 返回字节流
print(temp.text) #返回文本字符串
#endregion