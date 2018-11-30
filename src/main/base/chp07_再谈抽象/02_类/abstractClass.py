# 抽象基类
from abc import ABC, abstractmethod


class Talker(ABC):
    """抽象类(即包含抽象方法的类)不能被实例化"""

    @abstractmethod  # 将方法标记为抽象的,即在子类必须实现的方法
    def talk(self):
        pass


class Knigget(Talker):
    def talk(self):  # 子类继承后后若不实现父类的抽象方法则此类也是抽象类
        print("Knigget")


k = Knigget()
print(isinstance(k, Talker))
k.talk()


# 上述缺了让多态程度更高的部分,即只要实现talk,即便不是Talker的子类,仍然能通过类型检查
class Herring:
    def talk(self):
        print("Herring")


h = Herring()
Talker.register(Herring)
print(isinstance(h, Talker))
h.talk()


# 但是上述会存在一个缺点,就是直接从抽象类型派生提供的保障没有了,如下
class Clam:
    pass


Talker.register(Clam)
c = Clam()
print(isinstance(c, Talker))
c.talk()
"""
总结,isinstace返回True是一种意图的表达.
"""
