# 打开一个图片文件。
file = open("pic.jpg", 'rb') # 以二进制打开图片
print(file) # 输出创建的文件对象

# 打开文件时指定编码格式
# open打开文时默认用的时GBK编码，当打开不是GBK编码的文件时，会报错。
file = open('demo.txt', 'r', encoding='utf-8')
print(file)