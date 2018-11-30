class Parent:
    def init(self):
        print("父类初始化")

    def print(self):
        print("父类输出")


class Sub(Parent):  # 继承父类
    def init(self):
        """方法重载"""
        print("子类初始化")


class Mother:
    def init(self):
        print("母类初始化")

    def food(self):
        pass


class Daughter(Parent, Mother):
    """多重继承"""

    # 此处前一个继承的类的同名方法会覆盖后一个的同名方法(当多个超类的超类相同时,查找特定方法或属性时访问超累的顺序称为方法解析顺序即MRO)

    def primp(self):
        pass


subs = Sub()
subs.init()
subs.print()
# 判断类是否是另一个类的子类
print(issubclass(Sub, Parent))
# 查看类的父类
print(Sub.__bases__)
# 确定对象是否是某个类的实例
print(isinstance(subs, Sub))
print(isinstance(subs, Parent))
print(isinstance(subs, str))
