# 静态方法和类方法(在工厂函数中的用武之地),无需实例化即可调用
class MyClass:
    @staticmethod
    def static_method():
        print('this is static method.')

    @classmethod
    def class_method(cls):
        print('this is class method', cls)

    def m(self):
        print(self)


# 无需实例化即可调用
MyClass.static_method()
MyClass.class_method()
# 需要实例化才可调用
mc = MyClass()
mc.m()
