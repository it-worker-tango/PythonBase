# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 22:07:36 2018

@author: Tango
逻辑运算符
"""

# and 逻辑与 两边同时为真则为真
print("1 < 2 and 2 >0:", 1 < 2 and 2 > 0)
print("1 < 0 and 2 >0:", 1 < 0 and 2 > 0)
print("-" * 30)

# or 逻辑或 两边有一个为真则为真
print("1 < 2 or 2 >0:", 1 < 2 or 2 > 0)
print("1 < 0 or 2 >0:", 1 < 0 or 2 > 0)

print("-" * 30)
# not 逻辑非， 取反
print("not 1 < 2:{}".format(not 1 <2))