def userinfo(**info):
    for key, val in info.items():
        print("{}的年龄是{}".format(key, val))


userinfo(路飞='18', 乔巴='6')
print("---------------")
dict1 = {'路飞':18, '乔巴':6}
userinfo(**dict1) # 实参前面也需要加**