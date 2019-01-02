# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 22:06:45 2019

@author: Tango
break 
"""
flag = input("每次输入点东西，输入q时退出：")
while True: #一个死循环
    print(flag)
    flag = input("每次输入点东西，输入q时退出：")
    if flag == 'q':
        break #结束循环
