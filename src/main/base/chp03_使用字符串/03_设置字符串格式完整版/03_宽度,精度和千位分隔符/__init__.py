# 指定宽度

print('{num:10}.'.format(num=3))  # 指定数字宽度会在其前补空
print('{name:10}.'.format(name='Bob'))  # 指定字符串会在其后补空
from math import pi

print('{pi:10.2f}.'.format(pi=pi))  # 同时使用宽度和精度
print('{:.5}'.format('Guido van Rossum.'))  # 前五位
print('One googol is {:,}'.format(10 ** 100))  # 千位分隔符
