# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave  Base")

class A(Base):
    def __init__(self):
        print("enter Base")
        print("leave Base")


class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B,self)
        print("leave B")

class C(A,B):
    def __init__(self):
        print("enter c")
        super()



class Base(object):
   def __init__(self):
       print("enter Base")
       print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("----")
        print("leave A")


#为什么B类super不初始化呢
class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self)
        print("leave B")


class C(A,B):
    def __init__(self):
        # print("enter C")
        # print(super(A,self))
        # print("<------>1")
        # print(super(B,self))
        # print("<----->2")
        #print(C.self).__init__()
        # print((C,self).__init__()) 为什么这样打印不行呢 打印出了none
        print(C,self).__init__()
        print("<--------->3")
        print("leave C")

if __name__ == "__main__":
  c =C()
  C.__mro__
  #print(c.__mro__)
  #实例没有mro 类才有mro