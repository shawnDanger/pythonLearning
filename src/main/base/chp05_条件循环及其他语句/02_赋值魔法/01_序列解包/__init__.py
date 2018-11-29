# 序列解包(或可迭代对象解包):将一个序列(或任何可迭代对象)解包,并将得到的值存储到一系列变量中.
# 并行给多个变量赋值
x, y, z = 1, 2, 3
print(x, y, z)
# 交换多个变量的值
x, y = y, x
print(x, y, z)
values = 1, 2, 3
x, y, z = values
print(x, y)
scoundrel = {'name': 'Shawn', 'sex': 'man'}
key, value = scoundrel.popitem()
print(key, value)
# 注意解包时等号两边目标个数相同,否则将会报错ValueError: too many values to unpack
# 若想收集多余的值,可使用'*'收集
a, b, *c = [1, 2, 3, 4, 5]
print(c)
d, *e, f = [1, 2, 3, 4, 5]
print(e)
