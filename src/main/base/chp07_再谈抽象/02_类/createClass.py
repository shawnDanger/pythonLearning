class Person:
    name = 'join'

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print('hello,{}'.format(self.get_name()))

    def method(self):
        """此处是方法"""
        print("此处是方法!")

    def __private(self):
        print("私有方法")


def function():
    """此处是函数"""
    print("此处是函数!")


p = Person()
p.set_name("shawn")
p.greet()
# 函数赋值给方法
p.method = function
p.method()
# 函数赋值给变量
m = function
m()
# 访问私有方法->_类名__私有方法名
p._Person__private()
# 使用_方法名,在form module import * 中不会被导入
# dir(obj) return the names in the current scope 即返回当前scope的名字,包括类的命名空间.
# 类中定义的代码都是在特殊的命名空间(类的命名空间)执行的.
print(dir(p))
