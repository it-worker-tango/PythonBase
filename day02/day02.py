import keyword #引入关键字模块

print(keyword.kwlist) #获取关键字列表

#if = "我看看会发生什么"
#print(if)

num = 1024 # 创建变量num，该变量为数值类型
name = "路飞" #字符串类型的变量

myname, age = '路飞', 18
print(myname, age )

a = 0o123 # 八进制
print(a)

b = 0x25 # 十六进制
print(b) # 输出结果为37 不要误会为0乘以25

print(0.1 + 0.2) #对浮点数进行运算

print(0.1 == 0.1 )
print(0.2 == 0.2)
a = 0.1 + 0.2
print(a == 0.3) #这将是一个神奇的结果


title = "这是一个字符串" #使用双引号创建字符串
name = '路飞' #使用单引号创建字符串
#使用三个引号来创建字符串
word = """我是成为海贼王的男人！
海賊王に俺はなる！
"""
print(title)
print(name)
print(word)


print(True == 1)
print(True == 0)
print(False == 1)
print(False == 0)

# 模拟超市抹零结账
money_all = 56.7 + 32.9 + 87.52 #累加金额
money_all_str = str(money_all) #转换成字符串
print("总金额为："+ money_all_str)
money_real = int(money_all) #取整
money_real_str = str(money_real)
print("实收："+ money_real_str)

