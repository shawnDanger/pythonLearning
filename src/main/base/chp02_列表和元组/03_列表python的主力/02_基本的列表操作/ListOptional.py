print('基本列表操作')
print('1 修改列表:给元素赋值')
x = [1, None, 1, 1]
x[1] = 2
print(x)

print('2 删除元素')
del x[1]
print(x)

print('3 给切片赋值')
x[1:] = list('23')
print('覆盖原值1:' + str(x))
x[3:] = list('5')
print('末尾插入5:' + str(x))
x[3:3] = list('4')
print('中间插入4:' + str(x))
x[0:0] = list('0')
print('头部插入0:' + str(x))
x[3:7] = []
print('替换空值,与del等效' + str(x))
