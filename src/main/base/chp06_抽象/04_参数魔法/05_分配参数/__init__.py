# 与收集参数操作相反,此处为分配参数
def add(x, y):
    return x + y


# 列表和元组分配参数
params = [1, 2]
print(add(*params))


def hello(greeting, name):
    print(greeting, name)


ps = {'greeting': 'hello', 'name': 'shwan'}
hello(**ps)  # 字典分配参数
"""
如果参数只有列表和字典,可以不使用*或**,直接传递
"""
