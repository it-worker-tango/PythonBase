# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 21:47:58 2019

@author: Tango
for 循环
"""

# 遍历列表
for i in ['Python', 'C#', 'Java', 'VBA']:
          print(i)
          
# 计算1~100的和
print("1~10相加的和:")
result = 0
for i in range(101):#等价于 range(1, 101),以为不包括右边的数，所以是101，而不是100
    result += i # 等价于 result = result + i
print(result) # 5050