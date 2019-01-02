# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:34:54 2019

@author: Tango
and or not
"""

age = int(input("请输入你的年龄："))
if age >=18 and age <=70:
    print("你可以考驾照了。")
    
print("------------")
if age >= 18:
    if age <= 70:
        print("你可以考驾照了。")
        
# or
sales = int(input("请输入该商品的日销量："))
if sales < 20 or sales > 100:
    print("该商品销售异常，需要注意")
  
# not 
a = input("请输入一位数的密码：")
b = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
if a not in b:
    print("非法输入，请重新输入！")