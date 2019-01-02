import datetime # 引入Python的日期模块，后面会具体分析

print('当前年份：'+ str(datetime.datetime.now().year)) #输出当前的年，str()是将内容转换成字符串
#输出当前时间,注意代码中的引号，大小写
print('当前时间:' + datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'))