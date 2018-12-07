# 迭代文件内容
# 1.每次一个字节
with open('iterationFileContent.py', encoding='utf-8') as f:
    while True:
        char = f.read(1)
        if not char: break
        print(char)
# 2.每次一行
with open('iterationFileContent.py', encoding='utf-8') as f:
    while True:
        line = f.readline()
        if not line: break
        print(line)
# 3.读取所有内容
with open('iterationFileContent.py', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)
# 4.延迟迭代
import fileinput

for line in fileinput.input():  # 只负责打开文件
    print(line)
# 5.文件迭代器
# 文件都是可迭代的,迭代文件的结果是返回每一行(或其他)
