# 迭代器(和可迭代对象),本章简单介绍__iter__,它是迭代器协议的基础
# 迭代意味重复很多次,就像循环.
# 前面只是用for迭代过序列和字典,实际上可以迭代实现__iter__的对象

# 1.可迭代的迭代器
class Fibs:
    def __init__(self):
        self.a, self.b = 0, 1

    def __next__(self):
        """实现此方法的对象为迭代器"""
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        """实现此方法的对象为可迭代的"""
        return self


fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break
# 2.迭代函数iter
it = iter([1, 2, 3])
print(next(it))
print(next(it))


# 3.从迭代器创建序列
class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


ti = TestIterator()
print(list(ti))
