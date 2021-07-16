# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm

a=[1,2,5,3,47,2,5,7]
print(" Memory a:",id(a))
r=a.sort()
print(a,r)
r1=sorted(a)
print("r1:",r1)
print("Memory a:",id(a),"Memory r1:",id(r1))