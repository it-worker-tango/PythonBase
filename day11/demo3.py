with open("demo.txt", 'r') as file:
    file.seek(3) # 将光标移动到新位置
    string = file.read(8)
    print(string) # 运行结果：defghijk