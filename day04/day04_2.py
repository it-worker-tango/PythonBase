# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 22:05:50 2018

@author: Tango
元组
"""

# 使用赋值运算符创建
num = (1, 2, 3, 4)
print(num)
print(type(num)) #查看num的类型

# 创建空的元组
emptytuple = ()
print(type(emptytuple)) # 返回的依然是： <class 'tuple'>

# 删除元组
#del num # 同样使用del

# 访问元组
num = (1, 2, 3, 4, '路飞')
print(num[0]) #访问第一个元素
print(num[:3]) #获取前三个


print("修改前：", num)
num = (1, 3, 5) #重新赋值
print("修改后：", num)