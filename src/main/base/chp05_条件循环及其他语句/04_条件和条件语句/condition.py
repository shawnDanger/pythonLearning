"""
1.布尔值
判断时可直接使用False,None,0,(),[],{}都为假,其它都为真
但是假的互不相等,即() != {} 或 () != False
"""
print(True)
print(True == 1)
print(False == 0)
print(True + False + 42)
print(bool([]) == bool('') == False)
if [] == False:
    print(False)
elif [] == ():
    print(False)
elif [].__eq__(False):
    print('cc', True)
else:
    print("无结果")
"""
# 2.条件 ->if elif else 和代码块嵌套 
name = input('input your name:')
if name.endswith('shawn'):
    if name.startswith('Mr.'):
        print('Hello,Mr.shawn')
    elif name.startswith('Mrs.'):
        print('Hello,Mrs.shawn')
    else:
        print('unknown name!')
else:
    print('Hello,stranger')
"""
# 复杂条件
"""
1.比较运算符 
    >,<,=各种组合,!=不等于  比较的是值是否相等
    is 同一个对象   不可用于数和字符串,结果不可预测
    is not不同的对象
    in 是容器(如序列)的成员 
    not in 不是容器的成员
    注意: <,<=这种不兼容的类型比较必须是相近的类型,比如整型和浮点数
    可以链式比较
    都按照字母或数字顺序排列,否则按照Unicode字符比较
    
2.布尔运算符
    and
    or
    not
"""
code = ord("你")
print(code)
print(chr(code))
# 断言
age = 10
assert 0 < age < 100
age = -1
assert 0 < age < 100, 'age 必须大于零小于100'
