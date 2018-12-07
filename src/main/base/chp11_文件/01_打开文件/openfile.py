# 打开文件
filepath = 'openfile.py'
with open(filepath, 'r+', encoding='utf-8') as f:
    print(f.readlines())
"""
文件模式:
r 读取模式(默认值)
w 写入模式
x 独占写入模式
a 附加模式
b 二进制模式(与其他模式结合)
t 文本模式(默认值,与其他模式结合)
+ 读写模式(与其他模式结合)
"""
