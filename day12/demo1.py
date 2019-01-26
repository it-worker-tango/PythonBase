def division():
    num1 = int(input("请输入被除数：")) #接收用户输入的数据，并转换位int类型
    num2 = int(input("请输入除数："))
    result = num1 // num2 # 执行除法运算，且不要小数
    print(result)

if __name__ == "__main__":
    try:
        division() # 调用division()函数
    except ZeroDivisionError: # 捕获异常类型为ZeroDivisionError
        print("输入错误：除数不能为0")