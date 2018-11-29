print("三人行")
"""
pass 什么都不做
del 删除
exec,eval 执行字符串及计算其结果
"""
# 1.pass 什么都不发生,python中代码块不能为空,所以用pass做占位符
if 5 > 3:
    print("真的")
else:
    pass
# 2.del
"""
在python中,没有任何引用的字典将被python解释器直接删除,这成为垃圾收集
或者使用del直接将其删除,但删除的是变量名称,并没有删除字典本身,因为不在使用的值,python解释器会立即将其删除
"""
x = ['hello', 'world']
y = x
del x
print(y)
# 3.exec 将字符串作为语句进行执行或作为表达式进行计算,什么都不反悔
"""
注意,一般会为其加命名空间(作用域),一个全局(必须字典),一个局部(任何映射),否则会污染你的命名空间,即修改你的变量
"""
# 有命名空间
from math import sqrt

scope = {}
exec('sqrt = 1', scope)
print(sqrt(4), scope.keys())
# 无命名空间
x = 1
exec('x = 2')
print(x)
# 4.eval 计算用字符串表示的python表达式的值,并返回结果
a = 'a'
b = 'b'
print(eval('a<b'))
print(eval('1>2'))
