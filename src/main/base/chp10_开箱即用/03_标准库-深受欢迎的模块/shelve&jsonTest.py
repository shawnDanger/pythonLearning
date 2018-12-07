# shelve 将数据存储到文件中
import shelve, json

s = shelve.open('./shelve/shelveDataTest')  # 默认不会创建文件夹
s['x'] = ['a', 'b', 'c']
print(s['x'])
temp = s['x']
temp.append('d')
s['x'] = temp  # 添加入新的东西之后需要重新存储,即赋值,或者设置open函数中writeback为True(所有数据都读到缓存,即可以不用再重新存储,关闭shelve后自动写到本地文件)
print(s['x'])
s['a'] = temp
print(s['a'])
s['1'] = json.dumps({"name": 'shawn', 'age': 18, 'sex': 'man'})
print('json字符串:', json.loads(s['1']))
print('name:', json.loads(s['1'])['name'])
