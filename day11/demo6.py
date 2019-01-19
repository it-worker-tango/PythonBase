import os 

# name:用于获取操作系统的类型。 nt:windows posix,则表示为linux,Unix或者mac
print(os.name) # nt

# linesep: 用于获取当前操作系统的换行符
print(str(os.linesep)) # windows正常应该返回'\r\n',我这里由于某种原因没有显示出来

# sep用于获取当期系统的路径分割符
print(os.sep)

# 获取当前路径
print(os.getcwd()) # F:\笔记相关\Python基础第二次分享\day11

# 拼接路径
print(os.path.join(r"C:\user\code",'text.txt'))

# 检查路径是否存在
myPath = os.path.join(r"C:\user\code",'text.txt') # 进行路径拼接
print(os.path.exists(myPath)) # 返回值：False

# 遍历文件夹
dirs = os.walk(r"F:\笔记相关\Python基础第二次分享\day11")
for mydir in dirs:
    print(mydir)

# 重命名
src = r'F:\笔记相关\Python基础第二次分享\day11\old.txt'
newName = r'F:\笔记相关\Python基础第二次分享\day11\new.txt'
if os.path.exists(src): # 判断文件是否存在
    os.rename(src, newName)
    print("重命名完成")
else:
    print("文件不存在")

# 文件信息
if os.path.exists("msg.txt"):
    info = os.stat("msg.txt")
    print("文件大小:", info.st_size,"字节")
    print("最后一次修改时间:",info.st_mtime)