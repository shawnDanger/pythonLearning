# for循环
words = 'this is an ex parrot'.split()
print(words)
for word in words:
    print(word)
# 尽量使用for循环

# 1.迭代字典两种方式
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'value->', d.get(key))
for k, v in d.items():
    print(k, 'value->', v)
# 注意若使字典有序,可使用模块collections中的orderedDict类
# 2.迭代工具
#   1).并行迭代,java中则是嵌套for循环
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 14, 15, 23, 102]
# 拆包时最短序列使用完即不再缝合
iterator = zip(names, ages)
print(list(iterator))
# 此处必须在for里拆包,在外拆包不可用
for name, age in zip(names, ages):
    print(name, age)
#   2).迭代时获取索引
strings = ['shawn', 'join', 'anne', 'damon']
for index, string in enumerate(strings):
    if 'a' in string:
        strings[index] = index
print(strings)
#   3).反向迭代和排序后再迭代
# 使用reversed和sorted
# 注意reversed和zip一样返回一个神秘的对象,直接使用或list转换后使用列表的方法
