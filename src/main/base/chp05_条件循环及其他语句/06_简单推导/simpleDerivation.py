# 1.列表推导是一种从其它列表创建列表的方式,类似于集合推导
print([x * x for x in range(10)])
print([x * x for x in range(10) if x % 3 == 0])
print([(x, y) for x in range(3) for y in range(2)])
# 与下列方法相等
result = []
for x in range(3):
    for y in range(2):
        result.append((x, y))
print(result)
# 2.字典推导
squares = {i: "{} squared is {}".format(i, i ** 2) for i in range(10)}
print(squares.get(8), squares[8])
print(squares)
