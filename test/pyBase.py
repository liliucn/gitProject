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
