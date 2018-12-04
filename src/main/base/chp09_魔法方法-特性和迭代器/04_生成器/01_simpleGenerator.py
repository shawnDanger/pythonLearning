"""
生成器是一种使用普通函数语法定义的迭代器
包含yield语句的函数都被称为生成器
生成器可以生成多个值,每次一个.每次用yield生成一个值后,函数都将冻结,即在此停止执行,等待被重新唤醒,被重新唤醒后,函数将从停止的地方开始继续执行
"""
# 简单生成器
nested = [[1, 2], [3, 4], [5]]


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


print(list(flatten(nested)))
for num in flatten(nested):
    print(num)

# 生成器推导(生成器表达式)使用圆括号
"""
工作原理和列表推导相同,但不是创建一个列表(即不是立即执行循环),而是返回一个生成器,让你能够逐步进行计算
简单情景下,还不如使用列表推导,但要包装可迭代对象(可能生成大量的值),使用列表推导将立即实例化一个列表,从而丧失迭代的优势
"""
g = ((i + 2) ** 2 for i in range(2, 27))
print(next(g))
print(next(g))
s = sum(i ** 2 for i in range(10))  # 在已有的括号中则不必再添加括号
print(s)
