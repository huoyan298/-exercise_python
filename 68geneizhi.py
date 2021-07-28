# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
'''
# 将给的参数转为二进制
print(bin(10))
# 返回商和余数
print(divmod(20,3))
# 可迭代转为元组
print(tuple([1,2,3,4,5]))
# 返回翻转的迭代器
lst="你好啊"
it=reversed(lst)
# print(list(it))
# 列表的切片
a=("a","b","c","d","e","f","g","h")
(0,1,2,3,4,5,6,7)
x=slice(3,5)
# 第三位置开始，第5位置前切 ('d','e')
# print(a[x])
x=slice(0,8,3)
# 从0~8范围内，0开始，每过3个切一个。为嘛没有说切的步常 ('a','d','g')
# print(a[x])

# 根据字符串长度给列表排序
lst=['one','two','three','four','five','six']
def f(s):
    return len(s)

# 这里f位置有逗号 思考 ['one','two','six','four','five','three']
l1=sorted(lst,key=f,)
print(l1)
print("l1,lst:",id(l1),id(lst))

# 获取集合的枚举对象
lst=['one','two','three','four','five']
for index,el in enumerate(lst,1):
    print(index)
    print(el)

#zip(),将可迭代的对象作为参数，对应的对象打包成一个元组，
#如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同
lst1=[1,2,3,4,5,6]
lst2=['民','驴','春', '美', '护', '松']
lst3=['美','中国','法','意大利','韩','日']
# print(zip(lst1,lst2,lst3))
for e1 in zip(lst1,lst2,lst3):
    print(e1)

#
# s1=input("请输入a+b:")
# print(eval(s1))
#可以动态的执行代码，代码必须有返回值

# 文件操作相关 第一个参数是路径还是？这个要看看
# f=open('file',mode='r',encoding='utf-8')
# f.read()
# f.close()

# __immport__使用 延迟导入模块
class LazyImport:
    def __init__(self,module_name):
        self.module_name = module_name
        self.module = None

    def __getattr__(self, name):
        if self.module is None:
            self.module = __import__(self.module_name)
        return getattr(self.module,name)

time=LazyImport("time")
print(time.time())

import sys
#检查python的最低版本
if not sys.version_info >(2,7):
   print("<2.7")
elif not sys.version_info >= (3,5):
   print( "<2.7" )
else :
   print(">3.3")
   print(sys.version)

# 检查对象使用内存的状况
import sys
mylist = range(0,10000)
print(sys.getsizeof(mylist))
# 48
import  sys
myreallist=[x for x in range(0,10000)]
print(sys.getsizeof(myreallist))
# 87624

#合并
dict1={'a':1,'b':2}
dict2 ={'b':3,'c':4}
m={**dict1,**dict2}
print(m)
# 切片 0~2 [1,2]
first_two = [1,2,3,4,5][0:2]
print(first_two)
# 0~5 步长2 [1,3,5]
steps = [1,2,3,4,5][0:5:2]
print(steps)
# 翻转 cfbda
rever="adbfc"[::-1]
print(rever)
#全字符隔取一
mstring="abcdef fim ddfsdf"[::2]
print(mstring)


# 统计元素出现次数
from collections import Counter
mlist=[1,1,2,3,1,3,2,4,4,5]
c=Counter(mlist)
print(c)
# Counter({1: 3, 2: 2, 3: 2, 4: 2, 5: 1})
'''

# 拼接字符串和序列
import itertools
# import operator
# list(itertools.accumulate(range(1,11),operator.mul))
# print(list  .count())

a=['A','B','C']
b=['x','y','z']
c=a+b


l=itertools.chain(*c)
# 这里要思考下，遍历后，list(l)打印为[]
# for i in l:
#     print(c)

print(type(l))
print(list(l))

