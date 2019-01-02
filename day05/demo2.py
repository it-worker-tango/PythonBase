# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 22:08:14 2018

@author: Tango
正则表达式
"""
import re
# match
pattern = r'py_\w+' #匹配py_
string = 'PY_dsd py_tewt'
match = re.match(pattern, string, re.I) #re.I表示不区分大小写
print(match)
# 打印结果： <re.Match object; span=(0, 6), match='PY_dsd'>

# search()
search = re.search(pattern, string, re.I)
print(search)
# 打印结果： <re.Match object; span=(0, 6), match='PY_dsd'>

# findall
findall = re.findall(pattern, string, re.I)
print(findall) # ['PY_dsd', 'py_tewt'] findall 将返回一个列表

# 替换字符串 sub方法
pattern = r'1[34578]\d{9}'
string = '中奖号码为: python0001 联系电话为：13698989802'
result = re.sub(pattern, '1pythoner', string)
print(result) # 中奖号码为: python0001 联系电话为：1pythoner
