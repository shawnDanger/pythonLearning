# 作用域(命名空间) 类似于字典,vars()可以返回这全局作用域
print(vars())
x = 2
y = 3
scope = vars()
print(scope['x'])
print(scope['y'])

# 函数里经常与函数外名字重复,是因为调用函数时创建了一个新的命名空间,即局部命名空间,类似于java方法栈
# 若想访问方法外变量,直接在方法中使用其名字即可
z = 4
a = 5


def add(x):
    global a
    print(globals())
    print(vars())
    print(x, y, a, globals()['z'])


add(1)
"""
locals()会会返回局部作用域的字典
globals()会返回全局字典
"""


# 闭包
# 也叫作用域嵌套,,返回的是一个函数,而不是调用它
# 并且它携带这自己的作用域,即它带着自己所在的环境(和相关局部变量)
def multiplier(factor):
    ss = 3

    def multiplyByFactor(number):
        return number * factor + ss

    def modify():
        nonlocal ss
        # global ss
        ss = 5
        # def m():  # 可多层嵌套函数,并可以使用nonlocal修改外部变量
        #     nonlocal ss
        #     ss = 6
        # m()

    modify()  # 使用nolocal可修改modify方法外部变量(global不行)
    print(ss)
    return multiplyByFactor


double = multiplier(2)
print(double(2))
# 闭包内若要给外部变量赋值,需要加上nonlocal关键字,类似java静态内部类要加final
