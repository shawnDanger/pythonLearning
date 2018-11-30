# 未避免参数混淆,可以在调用参数时添加关键字参数,也可以指定默认值
def store(name, sex, phone):
    print(name, sex, phone)


def store2(name='shawn', sex='man', phone='123'):
    print(name, sex, phone)


def store3(name, sex='man', phone='123'):  # 此处默认参数应该放到正常参数后面
    print(name, sex, phone)


store('shawn', 'man', '1234')
store(name='shawn', phone='1234', sex='man')
store2()
store2(name='julia')
store3('join')
