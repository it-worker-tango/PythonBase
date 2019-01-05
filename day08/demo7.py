import math # 导入数学模块

def circlearea(r): #计算圆形的面积
    result = math.pi * r * r
    return result

r = 10 
print("半径为10的圆的面积是:", circlearea(10))

# 用匿名函数
r = 5
result = lambda r:math.pi * r * r
print("半径为5的圆的面积是", result(r))