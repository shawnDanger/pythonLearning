# 通用生成器
"""
生成器通常由两个单独的部分组成:生成器函数和生成器的迭代器,通常被视为一个,统称生成器
生成器被调用时不会执行函数体内的代码,而是返回一个迭代器,每次请求值时,豆浆执行生成器的代码,知道遇到yield或return
"""


def simple_generator():
    yield 1


print(simple_generator)
print(simple_generator())
