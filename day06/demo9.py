# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 22:15:32 2019

@author: Tango
演示逢7拍腿的游戏：就是所有人从1开始数，但数到7，或者包含7，或者是7的倍数时，
则不说出这个数改为拍腿。
"""

total = 99 #记录怕退的次数
mylist = [] #保存拍腿的数字
for number in range(1, 101): #从1数到100
    if number % 7 == 0:#7的倍数
        print("拍腿")
        mylist.append(number)
        continue
    else:
        string = str(number) #转成字符串，是为了判断是否包含7
        if string.find('7') > -1:
            print("拍腿")
            mylist.append(number)
            continue
        else:
            print(number) #说出该数字
    # 这个并不是每次都会执行到的。如果没有continue最终为-1 ，而
    # 有continue的情况，但执行continue时，该运算不会被执行
    total -= 1  
    
print("从1数到100共拍腿{}次\n其中拍腿的数字有:\n{}".format(total,mylist))
