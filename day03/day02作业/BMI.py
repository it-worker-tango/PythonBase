# -*- coding: utf-8 -*-
"""
根据身高，体重计算BMI指数。BMI = 体重 / (身高 X 身高)。
"""
height = input("请输入您的身高：") # 保存身高 ，单位米
print("您的身高：" + str(height))
weight = input("请输入您的体重:") #保存体重，单位千克
print("您的体重：" + str(weight))

bmi = float(weight) / (float(height) * float(height))
#判断身材是否合理
if bmi < 18.5:
    print("您的体重过轻")
if bmi >=18.5 and bmi <24.9:
    print("正常范围，注意保持")
if bmi >= 24.9 and bmi <29.9:
    print("您的体重过重")
if bmi >= 29.9:
    print("额，不知当讲不当讲，肥胖。。")