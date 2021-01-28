# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
# 重复元素判定
def all_unique(lst: object) -> object:
    return len(lst)==len(set(lst))

x=[1,1,2,2,3,2,3,4,5,6]
y=[1,2,3,4,5]

# 字符元素组成判定
from collections import Counter
def anagram(first,second):
    return Counter(first) ==Counter(second)


# 内存占用
import sys
variable = 30
# print(sys.getsizeof(variable))

#字节占用
def byte_size(string):
    return (len(string.encode('utf-8')))


# 打印N次字符串
n=2
s="Programming"

# 大写第一个字母
s="programming is awesome"
# print( s.title() )

# 分块
# 给定具体的大小，定义一个函数以按照这个大小切割列表
from math import ceil
def chunk(lst,size):
    return list(
        map(lambda x:lst[x*size:x*size+size],list(range(0,ceil(len(lst)/size)))))


# 压缩  这个方法可以将布尔值去掉，例如（false,None,0,"") 它使用filter()函数
def compact(lst):
    return list(filter(bool,lst))
compact([0,1,False,2,'',3,'a','s',34])

# 解包 如下代码可以将打包好的成对列表解开成两组不同的元组 这个
array = [['a','b'],['c','d'],['e','f']]
transposed = zip(*array)
# print(transposed)
# [('a','c','e'),('b','d','f')]

#链式对比
# 使用不同运算符对比多个不同的元素
a=3
# print(2<a<8)
# print(1==a<2)

# 逗号链接
hobbies=["baskerball","football","swimming"]
# print("My hobbies are:"+",".join(hobbies))

# 元音统计
# 以下方法将统计字符串中的元音（‘a','e','i','o','u')
# 原文 len(len(re.findall(r'[aeiou]',str,re.IGNORECASE)))
import re
def count_vowels(str):
    return len(re.findall(r'[aeiou]',str,re.IGNORECASE))

# 3
count_vowels('foobar')
# 0
count_vowels('gym')


# 首字母小写
# 首字符第一个字符小写
"""
def decapitalize(string):
    return str[:1].lower()

print(decapitalize("FooBar"))
# decapitalize('FooBar')
"""

# 展开列表通过递归的方式将嵌套展开为单额列表
"""
def spread(arg):
    ret=[]
    for i in arg:
     if isinstance(i,list):
        ret.extend(i)
     else:
        ret.append(i)
     return ret

def deep_flatten(lst):
     result =[]
     result.extend(spread(list(map(lambda x:deep_flatten(x) if type(x)==list else x,lst))))
     return result

print(deep_flatten([1,[2],[[3],4],5]))
"""
# 列表的差
def difference(a,b):
    set_a = set(a)
    set_b = set(b)
    comparison = set_a.difference(set_b)
    return  list(comparison)

# print(difference([1,2,3],[1,2,4]))

# 通过函数取差
# 会应用一个给定的函数,然后返回应用函数后结果有差别的表元素
def difference_by(a,b,fn):
    b=set(map(fn,b))
    return [item for item in a if fn(item) not in b]

from  math import floor
# [1.2]   [{x:2}]
# print(difference_by([2.1,1.2],[2.3,3.4],floor))
# print(difference_by([{'x':2},{'x':1}],[{'x':1}],lambda v:v['x']))

#链式函数调用 一行代码内调用多个函数
def add(a,b):
    return a+b

def subtract(a,b):
    return a-b
a,b=4,5
# print((subtract if a>b else add)(a,b))

# 检查重复項 将检查两个列表是不是有重复项
def has_duplicates(lst):
    return len(lst)!=len(set(lst))

x=[1,2,3,4,5,5]
y=[1,2,3,4,5]
# True false
# print(has_duplicates(x))
# print(has_duplicates(y))


# 合并两字典
def merge_two_dicts(a,b):
    c =a.copy()
    c.update(b)
    return c

a={'x':1,'y':2}
b={'y':3,'z':4}
# print(merge_two_dicts(a,b))

# 3.5更高版本
def merge_dictionaries(a,b):
  return {**a,**b}

a={'x':1,'y':2}
b={'y':3,'z':4}
# print(merge_dictionaries(a,b))

#将两个列表转化为字典
# 会将两列表转为单字典
def to_dict(keys,values):
    return dict(zip(keys,values))

keys=["a","b","c"]
values=[2,3,4]
# print(to_dict(keys,values))

# 使用枚举
# For 循环遍历列表 同样我们也能枚举列表的索引与值
"""
list =["a","b","c","d"]
for index,element in enumerate(list):
     print("value",element,"Index",index,)
"""

# 执行时间
import time
start_time = time.time()
a=1
b=2
c=a+b
print(c)
end_time = time.time()
total_time = end_time - start_time
print("%s%s%s",start_time,end_time,total_time)

# 23 Try else  这个。。
# try/except 也可加一else

def try_except_catch():
  try:
      2*3
  except TypeError:
     print("An exception was raised")
  else:
     print("Tank God,no exception were raised")


# 元素频率
# 元素频率取列表中最常见的元素
def most_frequent(list):
    return max(set(list),key=list.count)

list = [1,2,2,1,3,2,1,4,2]
print(most_frequent(list))

# 回文序列
def palindrome(string):
    from re import sub
    s=sub('[\W_]','',string.lower())
    return s ==s[::-1]

print(palindrome('taco cat'))

# 不使用if-else的计算子
# 不使用条件语句就实现加减乘除，求幂操作 通过字典这一数据
import operator
action={
    "+":operator.add,
    "-":operator.sub,
    "/":operator.truediv,
    "*":operator.mul,
    "**":pow
}

print(action['-'](50,25))


# shuffle
# 该算法会打乱列表元素的顺序，它主要会通过 fisher_yates
from copy import deepcopy
from random import randint
def shuffle(lst):
    temp_lst = deepcopy(lst)
    m=len(temp_lst)
    while (m):
        m-=1
        i = randint(0,m)
    temp_lst[m],temp_lst[i]=temp_lst[i],temp_lst[m]
    return temp_lst

foo = [1,2,3]
shuffle(foo)
print(shuffle(foo))

# 展开列表*******
# 将列表内的所有元素 包括子列表，都展开成一个列表
"""
def spread(arg):
   ret=[]
   for i in arg:
       if isinstance(i,list):
           ret.extend(i)
       else:
           ret.append(i)
       return ret

print(spread([1,2,3,[4,5,6],[7],8,9]))


# 29交换值
# 不需要额外操作就交换两个变量的值
def swap(a,b):
    return b,a

a,b = -1,14
swap(a,b)
spread([1,2,3,[4,5,6],[7],8,9])
"""


# 30 字典默认值
# key-value get() 那么如果遇到不存在的 key 则返回NOne
d={'a':1,'b':2}
print(d.get('c',3))



if __name__=="__main__":
    '''
    print(all_unique( x ))
    print(all_unique(y))
    
    print(anagram( "abcd3", "3acdb" ))

    print( sys.getsizeof( variable ) )
    print(byte_size(''))
    print(byte_size('z'))
    print(byte_size( '你' ))
    
    print(s*n)

    print( s.title() )
    
    print(chunk( [1, 2.3, 4, 5], 2 ))
    
    print(compact( [0, 1, False, 2, '', 3, 'a', 's', 34] ))
    
    print(count_vowels('foobar'))
    print(count_vowels('gym'))
    '''
    # print( difference( [1, 2, 3], [1, 2, 4] ) )

    # print( (subtract if a > b else add)( a, b ) )
    # print( merge_two_dicts( a, b ) )

    print( to_dict( keys, values ) )