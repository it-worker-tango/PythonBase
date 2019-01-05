def hello(*name):
    '''
    注意这里的形参前面有一个*
    表示接受任意数量的name
    '''
    print('形参name的类型', type(name))
    for item in name:
        print("{}，你好".format(item))
print('------一个实参------')
hello('路飞')
print('------2个实参------')
hello('路飞','乔巴')
print('------3个实参------')
hello('路飞','娜美', '乔巴')