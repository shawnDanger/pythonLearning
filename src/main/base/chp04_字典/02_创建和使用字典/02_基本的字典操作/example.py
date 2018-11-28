# 一个简单的数据库
# 一个将人明用作键的字典,每个人都用一个字典表示,
# 字典包含键'phone'和'addr',他们分别于电话号码和地址相关联
people = {
    'alice': {
        'phone': '123',
        'addr': '地址一'
    },
    'shawn': {
        'phone': '321',
        'addr': '地址二'
    }
}
# 电话号码和地址的描述性标签
lables = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('input your find name: ')
attr = input('phone(p) or address(a)? ')
if attr == 'p': key = 'phone'
if attr == 'a': key = 'addr'
if name in people: print("{}'s {} is {}".format(name, lables[key], people[name][key]))
