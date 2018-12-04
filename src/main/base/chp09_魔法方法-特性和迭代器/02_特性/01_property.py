# 特性是通过存取方法定义的属性
# python可以帮你隐藏存取方法,让所有属性看起来都一样
# property


class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size

    def get_size(self):
        return self.width, self.height

    # 可以简化使用操作
    size = property(get_size, set_size)


r = Rectangle()
r.width = 10
r.height = 5
print(r.get_size())
r.set_size((120, 100))
print(r.get_size())

# 简化后像正常属性一样
r1 = Rectangle()
r1.width = 10
r1.height = 5
print(r1.size)
r1.size = 150, 120
print(r1.size)
