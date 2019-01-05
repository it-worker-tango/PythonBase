def userInfo(name, age, height):
    '''
    定义一个方法，接收名字，年龄以及身高
    并打印出来
    '''
    print("姓名:{}\n年龄:{}\n身高:{}".format(name, age, height))


# 调用函数
userInfo('路飞', 18, 175)
print('----------错误演示----------')
# 错误演示，位置错误
userInfo(18, '路飞', 175)

print('----------关键字参数----------')
# 关键字参数
userInfo(age = 18, name='路飞', height= 175)

def userInfo2(name, age, height=170):
    '''
    定义一个方法，接收名字，年龄以及身高
    并打印出来
    height=170 就是为参数指定了默认值
    '''
    print("姓名:{}\n年龄:{}\n身高:{}".format(name, age, height))

userInfo2(age = 18, name='路飞', height= 175)
print('--------使用默认值--------')
userInfo2(age = 18, name='路飞')