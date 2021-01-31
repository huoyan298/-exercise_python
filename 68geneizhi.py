# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
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
# print(l1)

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