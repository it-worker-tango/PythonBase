# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:26:07 2018

@author: Tango
序列
"""

names = ['路飞', '娜美', '乔巴']
print(names[1]) #这里的1就是索引
print(names[-1]) #-1表示从右边数第一个

names = ['路飞', '娜美', '乔巴', '索隆', '山治', '布鲁克']
print(names[1:5]) #获取第二个元素到第5个元素的内容
print(names[0:5:2]) #获取第1， 3， 5个元素

names1 = ['路飞', '娜美', '乔巴', '索隆', '山治', '布鲁克']
names2 = ['鸣人', '小樱']
print("names1 + names2:",names1 + names2) #将连个序列相加

nums = [1, 2, 3, 4]
print("nums + names2:",nums + names2) #将连个序列相加

phone = ['锤子', '华为', 'VIVO']
print("phone * 3:",phone *3) #将会重复输出3次phone的内容，并生产一个新的序列

names = ['路飞', '娜美', '乔巴', '索隆', '山治', '布鲁克']
print("路飞在names里吗：", '路飞' in names)
print("路飞不在names里吗：", '路飞' not in names)

nums = [1, 2, 3, 4, 78, 21, 12, 43, -32]
print("nums的长度为：",len(nums)) #获取nums的长度，即包含几个元素

print("nums中最大的是:",max(nums)) #获取nums的最大值
print("nums中最小的是:", min(nums)) #获取nums的最小值