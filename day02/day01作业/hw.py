## day01 作业:根据用户输入的出生年份，判断是否成年

import datetime #调入时间模块

myYear = input("请输入您的出生年份：") #输入出生年份，必须是4位数，如：1988
nowYear = datetime.datetime.now().year #计算当前年份
age = nowYear - int(myYear) # 用于计算实际年龄
print("您的年龄为："+str(age) +"岁") #输出年龄

#根据计算的年龄所处的年龄段，判定标准是根据联合国组织给出的新年龄分段判断标准
if age < 18: #如果年龄小于18岁
    print("您还未成年")
if age >= 18 and age < 66: # 如果年龄大于等于18小于66岁
    print("您现在为青年人")
if age >= 66 and age < 80: #如果年龄大于等于66小于80岁
    print("您现在为中年人")
if age >= 80: #如果年龄大于80岁
    print("您现在为老年人")