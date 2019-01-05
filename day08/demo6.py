message = '你好'

def msg():
    print("函数内部：",message)
msg()
print("函数外部：",message)

def showMsg():
    global errMsg
    errMsg = "我变成了全局变量"
showMsg()
print(errMsg)