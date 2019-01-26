def division():
    num1 = int(input("请输入被除数：")) #接收用户输入的数据，并转换位int类型
    num2 = int(input("请输入除数："))
    result = num1 // num2 # 执行除法运算，且不要小数
    print(result)

if __name__ == "__main__":division() # 这个程序的入口，并调用division函数