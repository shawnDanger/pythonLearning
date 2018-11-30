# 允许用户提供多个参数,*param,提供的是元组方法
def parmas(*params):
    print(params)


parmas(1, 2, 3, 4, 5)
parmas(1)


# *可收集除title,end的余下params参数,*不会收集关键字参数
def params(tile, *params, end):
    print(tile, params, end)


params('标题', 1, 2, 3, end='结尾')


# *收集关键字参数需要**,收集的是字典,参数列表中只可以存在一个**
def parmas3(title, **parmas):
    print(title, parmas)


parmas3('b标题', content='内容', end='结尾')


# 综合使用
def parmas4(x, y, z=3, *params, **kv):
    print(x, y, z)
    print(params)
    print(kv)


parmas4(1, 2, 4, 5, 6, 7, name='shawn', sex=17)
