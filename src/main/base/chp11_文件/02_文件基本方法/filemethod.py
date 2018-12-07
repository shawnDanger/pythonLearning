# 文件的基本方法 with 可自动关闭文件,即使有异常
# 1.读取和写入(单字和行)
with open('file.txt', 'w') as f:
    f.write('Hello, ')
    f.write('world!')
    f.writelines('i use python')
    # 可随机存取,即不是从头到尾读取文件流
    # seek将当前位置移动到指定位置
    # tell当前文件处于什么位置
with open('file.txt', 'r+') as f:
    print(f.read(4))
    print(f.read(10))
    print(f.readline())
    f.write('you!')

# 2.管道重定向输出 管道:将一个命令的标准输出连接到下一个命令的标准输入.
import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('wordcount:', wordcount)
#  windows下执行type filemethod.py | python filemethod.py 查看自身文件的单词个数
# 3.with 它可以打开文件并赋给变量,且到达末尾自动关闭文件,专门为此设计的语句
