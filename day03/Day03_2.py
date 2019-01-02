# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 21:50:00 2018

@author: Tango
"""

# = 简单的赋值运算符
x = 20
y = x
print("x:",x)
print("y:",y)
print("-" * 30)
# =+ 加赋值 x+=y 等价于 x= x +y
x += y
print("x:",x)
print("y:",y)
print("x+=y:",x)

print("-" * 30)
# -= 减赋值 x-=y 等价于 x=x -y
x = 20
y = 5
x-=y
print("x:",x)
print("y:",y)
print("x-=y:",x)

print("-" * 30)
# *= 乘赋值 x*=y 等价于 x = x *  y
x = 20
y = 5
x*=y
print("x:",x)
print("y:",y)
print("x*=y:",x)

print("-" * 30)
# /= 出赋值， x/=y 等价于 x = x/y
x = 20
y = 5
x/=y
print("x:",x)
print("y:",y)
print("x/=y:",x) #注意Python运行除法的结果实浮点型

#其他运算也一样，大家试试 %=, **= //=