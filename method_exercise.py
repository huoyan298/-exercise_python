# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import requests
# url='https://www.python.org/static/img/python-logo@2x.png'
# myfile = requests.get(url)
# open('c:/users/LikeGeeks/downloads/PythonImage.png','wb').write(myfile.content)


# 判断奇偶数
num = int(input ("请输入一个数:"))
if num%2 ==0:
    print('%d是偶数'%num )
else:
    print('%d不是偶数'%num)

# 九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%s*%s=%s'%(i,j,i*j),end='')
    print()

# 生成日历
# import calendar
# yy=int(input("输入年份： "))
# mm = int(input("输入月份: "))
# print(calendar.month(yy,mm))

# 中文也可以做变量
姓名 = "我是python猫"
print( f"中文也可以做变量，{姓名},欢迎关注!" )


if __name__=="__mian__":
 print(1)