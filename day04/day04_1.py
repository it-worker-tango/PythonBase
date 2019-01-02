# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 20:58:28 2018

@author: Tango
列表
"""
#使用赋值运算符创建列表
numList= [7, 3, 2, 3]
print(numList)

emptyList = [] #创建空的列表

#创建数值列表
numList2 = list(range(10, 20, 2)) #range(10, 20, 2)表示从10~20，每次增加2个
print(numList2)

#del 删除对想
print("-----删除前-----")
print(numList)
print("-----删除后-----")
#del numList
#print(numList)

#用for循环遍历列表
namelist = ['路飞', '娜美', '乔巴', '索隆', '山治', '布鲁克']
for item in namelist:
    print(item)
    

print("2018年俄罗斯世界杯四强:")
team = ['法国', '比利时', '英格兰', '克罗地亚']
for index,item in enumerate(team):
    print(index + 1,item)

# 添加元素
print("添加前的namelist：", namelist)
namelist.append('弗兰奇')
print("添加后的namelist：", namelist)

print("添加前的namelist：", namelist)
newList= ['女帝']
namelist.extend(newList)
print("添加后的namelist：", namelist)

# 使用del删除元素
print("删除前的namelist：", namelist)
del namelist[-1]
print("删除后的namelist：", namelist)

#根据元素值删除
print("删除前的namelist：", namelist)
namelist.remove('路飞') #删除路飞
print("删除后的namelist：", namelist)

remVal = '女帝' #这个是不存在的
if namelist.count(remVal) > 0:
    namelist.remove(remVal) #没有进行判断
print(namelist)


# 获取指定元素出现的次数
namelist = ['路飞', '娜美', '乔巴', '索隆', '山治', '布鲁克']
namelist2 = ['路飞',  '索隆', '山治', '布鲁克']
namelist.extend(namelist2)

print("索隆出现了：",namelist.count('索隆'),"次") #统计索隆出现的次数

print("索隆第一次出现的下标:",namelist.index("索隆"))

numlist = [1, 2, 3, 44, 5, 34,23]
print("numlist所有元素的和：", sum(numlist))

# 对numlist排序
print("排序前：", numlist)
numlist.sort()
print("排序后：", numlist)

numlist = [1, 2, 3, 44, 5, 34,23]

numlist_as = sorted(numlist) # 升序，默认
print("numlist升序排列:", numlist_as)
numlist_des = sorted(numlist, reverse = True)
print("numlist降序排列:", numlist_des)

# 列表推导式
newnums = [int(x * 2) for x in numlist]
print(newnums) #numlist的元素乘以2 生成性的列表

# 添加判断条件
newnums = [int(x * 2) for x in numlist if x < 10]
print(newnums) #numlist的元素乘以2 生成性的列表







