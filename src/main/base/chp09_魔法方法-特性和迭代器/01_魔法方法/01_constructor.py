# 构造函数(constructor)__init__(在创建对象时调用)
class FooBar:
    def __init__(self):
        """__init__(在创建对象时调用)"""
        self.var = 42


fb = FooBar()
print(fb.var)


# 析构函数(destructor)__del__(在对象呗销毁前调用,即在被作为垃圾回收前)
class FooBar2:
    def __init__(self, value='42'):
        self.var = value

    def __del__(self):
        """__del__(在对象呗销毁前调用,即在被作为垃圾回收前)"""
        print('被摧毁')


fb1 = FooBar2()
fb2 = FooBar2('this is value')
print(fb1.var)
print(fb2.var)
