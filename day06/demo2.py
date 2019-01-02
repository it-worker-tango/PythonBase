# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:14:55 2019

@author: Tango
if else 语句
"""

number = int(input("请输入您的QQ号：")) 
if number == 182133566:
    print("恭喜中奖了！")
else:
    print("很遗憾没有中奖")
    
msg = "恭喜中奖了!" if number == 182133566 else "很遗憾没中奖" 
print(msg)