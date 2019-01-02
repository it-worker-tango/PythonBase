a = 1024 #变量a，值为1024
b = 5 #变量b，值为5
print(9) #输出数字9
print(a * b) #输出a * b 的结果，* 为乘法运算
print("go big or go home") # 输出"go big or go home"，注意引号为英文引号

print(a, b, "go big or go home")   #一次输出多个内容


fp = open(r'F:\day01.txt','a+') #打开要写入的文件
print("要么出众，要么出局", file = fp)#写入内容
fp.close() #关闭文件