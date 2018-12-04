class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):
        if key == 'size':
            self.width, self.height = value
            print('set', key, value)
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        if item == 'size':
            print('get', self.width, self.height)
            return self.width, self.height
        else:
            raise AttributeError


r = Rectangle()
r.size = 12, 13
# r.__setattr__('size', (20, 10))
print(r.size)
"""
getattribute 在属性被访问时自动调用
getattr 在属性被访问而对象没有这样的属性时自动调用
setattr 试图给属性赋值时自动调用
delattr 视图删除属性时自动调用
"""
