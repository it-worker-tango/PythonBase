class Dog:
    _color = '黑色' #私有属性
    def __init__(self):
        print("__init__:", Dog._color) # 在私立方法中访问私有属性

myDog = Dog()
print("直接访问", myDog._color)

