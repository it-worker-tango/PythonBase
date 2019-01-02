# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 20:40:19 2018

@author: Tango
"""
str1 = "hello"
str2 = 'Python'

print("str1 + str2:",str1 + str2)

#计算字符串的长度
str1 = "人生苦短，我用Python"
print("str1的长度：", len(str1))

#截取字符串
print("原始字符串:", str1)
print("第一个字符:", str1[0]) 
print("第3个到第5个字符：", str1[2:5])


# 分割字符串
str1 = "I love Python"
list1 = str1.split()
print(list1) #['I', 'love', 'Python']

str2 = "I love Python,java,C#"
list2 = str2.split(',')
print(list2) # ['I love Python', 'java', 'C#']


# 检索字符串
# 利用count函数
str1 = "@Python @java @C#"
print('字符串',str1,"中@符号出现了", str1.count('@'), '次')
# 打印结果：字符串 @Python @java @C# 中@符号出现了 3 次

# find 获取指定字符首次出现的索引位置
print("字符串:", str1, "中@第一次出现的位置是：", str1.find("@"))
# 打印结果：字符串: @Python @java @C# 中@第一次出现的位置是： 0

# index 获取指定字符首次出现的索引位置
print("字符串:", str1, "中@第一次出现的位置是：", str1.index("@"))
# 打印结果：字符串: @Python @java @C# 中@第一次出现的位置是： 0

# 在str1中查找！号
print(str1.find('!')) # 结果-1

# print(str1.index('!')) # ValueError: substring not found

# startwith() 判断是否以指定字符开头
str1 = "@Python @java @C#"
print(str1.startswith("@")) # True


# endswidth() 判断是否以指定字符结尾
print(str1.endswith('#')) #True

# 大写变小写
str1 = "ABCDEFG"
print(str1.lower()) # 打印结果abcdefg
# 小写变大写
str1 = "qwertyuiop"
print(str1.upper()) # 打印结果：QWERTYUIOP

#strip 去左右空格
str1 = "     Python    "
print(str1.strip()) # 打印结果Python

# lstrip 去左边空格
print(str1.lstrip()) #'Python    '

#rstrip 去右边空格
print(str1.rstrip()) #      Python

# 去掉左右的#好
str1 = "# asdfgh #"
print(str1.strip('#')) #  asdfgh 
                 
name = '路飞'
age = 18
print("{}的年龄是{}".format(name, age)) # 路飞的年龄是18












