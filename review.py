# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm

#sum 1-100
print(sum(range(1,101)))
#去除首字母
L=' I love you'
print(L)
print(L.strip())
#相反排序
num=[1,4,5,65,99,43]
num.reverse()
print("num"+str(num))

#一个元素的元组加逗号
t=(1)
print(type(t))
t=(1,)
print(type(t))
#两个斜杠私有方法，用from module import *导入时不会导入私有方法
class Person:
    def __name(self):
        print('私有方法')

    def print_P(self):
        self.__name()

p=Person()
p.print_P()


# 判断一个类是否是另一个类的子类
class A:
    pass
class B(A):
    pass

print(issubclass(B,A))

#
import random
li=[1,'two','3','四']
# 随机
print(random.choice(li))
# 删除
li.remove('3')
print(li)
# 查通过from xx import xx 导入的可以直接调用的方法
import random
print(random.__all__)

# 两个集合的并集
a={6,7,8}
b={8,9,60}
a.union(b)
print(a)

# 文件中写入字符
with open('hel.txt','w') as f:
    f.write('hello world')
print(f)

with open('hel.txt','r') as f1:
    print(f1.read())

# 查看f1的编码
print(f1.encoding)
# 获取路径下所有目录名称
import sys
print(sys.path)

# 将当前时间转为字符串
import time
print(time.asctime())
# 用切片将对象倒序
s="basketball"

print(s[::-1])

# *=创建新序列
t=(1,2,3)
print(id(t))
t*=2
print(t)
print(id(t))

# sort 原序列上 sorted 新建一序列
l=[1,2,9,4]
j=l.sort()
k=sorted(l)
print(j,k)
#n种字典创建方法
a=dict(one=1,two=2,three=3)
b={'one':1,'two':2,'three':3}
c=dict(zip(['one','two','three'],[1,2,3]))
d=dict([('two',2),('one',1),('three',3)])
e=dict({'one':1,'two':2,'three':3})
print(a,b,c,d,e)
# 列表去重
l={'A','B','A','B'}
print(list(set(l)))

#
m={'A','B','C','D','E'}
n={'B','C','D'}
found =0
for i in m:
 print(i)
 if i in n:
     found+=1

print(found)

#用递归实现阶乘
def factorial(n):
    """return n!"""
    return 1 if n<2 else n*factorial(n-1)

# 装饰器  判断对象是否可被调用
print([callable(obj) for obj in (abs,str,2)])

#值，地址
a=[1,2,3]
b=[1,2,3]
print(a==b,a is b)
print(isinstance(a,tuple))