class Rect:
    def __init__(self, width, height):
        self.width = width #矩形的宽
        self.height = height # 矩形的高
    @property
    def area(self):
        return self.width * self.height #计算矩形的面积

rect = Rect(10, 20)
print("面积为:", rect.area)
