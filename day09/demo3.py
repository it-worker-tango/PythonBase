class Dog:
    '''Dog类'''
    leg = '4条腿跑的快'
    def __init__(self):
        print("这是一个Dog类")
        print(Dog.leg)

# 访问类属性
myDog = Dog()


class Car:
    '''汽车类'''
    def __init__(self):
        self.color = '黑色'
        print(self.color)

car1 = Car()
car2 = Car()
print("car1的颜色",car1.color)
car2.color = "红色"
print("car2的颜色",car2.color)