class Fruit:
    def __init__(self, color='绿色'):
        Fruit.color = color

    def harvest(self):
        print("水果是", Fruit.color , '的。')
        print("水果已经获得")
        print('水果原来是',Fruit.color,'的。')

class Orange(Fruit):
    color = '橙色'
    def __init__(self):
        print("\n我是橘子")

class Apple(Fruit):
    color = '橙色'
    def __init__(self):
        print("\n我是苹果")  
        super().__init__()     

orange = Orange()
# orange.harvest() # 会报错 type object 'Fruit' has no attribute 'color'
apple = Apple()
apple.harvest()