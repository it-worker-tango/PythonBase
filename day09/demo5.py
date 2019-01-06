class Dog:
    __color = "黑色" # 私有属性
    def __init__(self):
        print("__init__:", Dog.__color)

myDog = Dog()
print("通过类名访问", myDog._Dog__color) #私有属性可以通过实例名._类名__xx的方式访问
print("直接访问:", myDog.__color) # 这里会报错