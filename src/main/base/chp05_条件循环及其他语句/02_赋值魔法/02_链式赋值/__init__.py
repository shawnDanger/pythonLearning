# 链式赋值是一种快捷方式,用于将多个变量关联到同一个值.
x = y = len("1")
print(x, y)
# 与下面赋值方式相同
y = len("1")
x = y
print(x, y)
# 与下面赋值方式不同
y = len("1")
x = len("1")
print(x, y)
