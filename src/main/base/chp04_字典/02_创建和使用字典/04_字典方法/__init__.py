# 1.clear 清除字典
# 普通删除采用赋值给x,原有字典不会被删除,并且y引用指向它
x = {}
y = x
x['key'] = 'value'
print(y)
x = {}
print(y)
# 完全删除使用clear,原有字典会被删除,y也为空
a = {}
b = a
a['key'] = 'value'
print(b)
a.clear()
print(b)
# 2.copy 返回一个新字典
print('浅复制')
#   键值对也使用原有字典的引用(修改新字典引用中的值,原有值也会变化)
x = {'username': 'shawn', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'deng'
y['machines'].remove('bar')
print(x)
print(y)
print('深复制')
# 完全复制所有键值及其所包含的所有值
from copy import deepcopy

x = {'username': 'shawn', 'machines': ['foo', 'bar', 'baz']}
y = deepcopy(x)
y['username'] = 'deng'
y['machines'].remove('bar')
print(x)
print(y)
# 3.fromkeys 创建一个新字典,包含指定的键,或默认所有键为None
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], 'I do not know'))
# 4.get 访问字典项
print('get:' + str(x.get('size')))
print('get:' + str(x.get('username', '空值')))
print('get:' + str(x.get('size', '为空时的默认值,不会影响真实值')))
# print(x['size'])

# 5.items返回一个包含所有字典项的列表,每个元素都为(key,value)形式,排列顺序不确定
d = {'title': 'My Home Page', 'url': 'http://www.python.org', 'sp': 0}
items = d.items()
print(items)  # 返回值为字典视图的特殊类型
print(len(items))
print(('title', 'My Home Page') in items)
# 字典视图(始终映射底层字典),不复制
d['sp'] = 1
print(('sp', 1) in items)
d['sp'] = 0
print(('sp', 0) in items)
# 复制字典视图
print(list(d.items()))
# 6.keys
print(d.keys())
# 7.pop 获取指定键的值,并删除其键值
print(d.pop('sp'))
# 8.popitem随机逐个弹出字典项,用于高效删除并处理所有字典
print(d.popitem())
# 9.setdefault 与get方法一样,但多了使用此方法是,字典不包含指定键时,会在字典中添加指定的键值对,若参数只有一个时,默认值为None
d = {}
print(d.setdefault('sex', "男"))
print(d.setdefault('sex', '默认'))
print(d.setdefault('name'))
print(d)
# 10.update 使用一个字典中的项来更新另一个字典
e = {'name': 'shawn'}
d.update(e)
print(d)
# 11.values 返回一个由字典中的值组成的字典视图(可能包含同样的值)
f = {}
f[1] = 1
f[2] = 2
f[3] = 3
f[4] = 1
print(f.values())
