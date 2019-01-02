# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:30:35 2019

@author: Tango
if 嵌套
"""

number = int(input("请输入去年的销量:"))

if number >= 1000:
    print("销量不错")
else:
    if number >= 500:
        print("销量还过得去")
    else:
        print("还需要努力啊")

