# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import time
import random
from multiprocessing import Queue,Process

def consumer(name,q):
    while True:
     res = q.get()
     if res is None: break
     time.sleep(random.randint(1,3))
     print("消费者%s,开吃%s"%(name,res))

def producer(name,q):
    for i in range(5):
        time.sleep(random.randint(1,2))
        res="大虾%s"%i
        q.put(res)
        print("生产者%s生产%s:"%(name,res))

if __name__=="__main__":
    q=Queue()
    p1 =Process(target=producer,args=("chihuo",q))
    p2 =Process(target=producer,args=("chihuo2",q))
    p3 =Process(target=producer,args=("chihuo3",q))

    c1=Process(target=consumer,args=("lilei",q))
    c2=Process(target=consumer,args=("hanmeimei",q))

    p1.start()
    p2.start()
    q.put(None)
    q.put(None)

