# 探索模块
# 导入某包,若不报错,则继续探究
# 1.dir 查看模块包包含哪些东西:所有属性(对于模块,它列出所有的函数,类,变量等)
import copy, pprint

pprint.pprint(dir(copy))
pprint.pprint([n for n in dir(copy) if not n.startswith('_')])  # 简单列表推导
# 2.__all__  可以直接通过此方法询问模块包含哪些内容
pprint.pprint(copy.__all__)
print(copy.deepcopy([1, [2, [5]], 3, 4]))
# 3.使用help获取帮助
# print(help(copy))
# print(help(copy.copy))
# print(help(copy.copy.__doc__))
# print(help(copy.__doc__))
# 4.文档(Python库参考手册(https://docs.python.org/library))
print(copy.__doc__)
# 5.使用源代码
# 查看cope的文件路径
print(copy.__file__)
