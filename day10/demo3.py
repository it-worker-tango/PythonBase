hello = "你好啊朋友" # 定义一个全局变量
def read():
    '''看书的功能'''
    hello = '你好啊朋友，一起看书吧。'
    print(hello)

if __name__ == "__main__":
    print("我去书店。。。。")
    read()
    print("我回家...")
    hello = "吃饭。。。"
    print(hello)