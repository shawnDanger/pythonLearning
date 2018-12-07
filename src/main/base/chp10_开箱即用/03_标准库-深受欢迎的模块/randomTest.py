# random生成伪随机数的函数(真随机是os.urandom函数)
from random import *

# 1.random() 返回0~1
print('random', random())
print(getrandbits(3))  # 以整数的形式返回指定数量的二进制位
# 2.uniform(a,b)返回一个a~b的随机实数
print('uniform', uniform(1, 10))
# 3.randrange()从range()中随机选择一个数
print('randrange', randrange(0, 20, 2))
# 4.choice从序列随机选择
seq = [1, 3, 5, 2, 4, 2]
print(choice(seq))
# 5.shuffle就地打乱序列
shuffle(seq)
print(seq)
# 6.从序列随机选择n个值不同的元素
print(sample(seq, 3))

from time import *

# 例子1:生成时间段内的时间
date1 = (2016, 1, 1, 0, 0, 0, -1, -1, -1)
time1 = mktime(date1)
date2 = (2018, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(date2)
print(asctime(localtime(uniform(time1, time2))))
# 例子2:随机文件内容
import fileinput

fortunes = list(fileinput.input())
print('随机文件中的行', choice(fortunes))
# cmd执行python randomTest.py file1.py |[文件名2]
