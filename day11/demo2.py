# 读取文件中的指定个数的字符
with open("demo.txt", 'r') as file:
    string = file.read(3) # 读取前3个字符
    print("前3个字符为:", string) # 运行结果：前3个字符为: abc