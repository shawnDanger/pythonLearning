# 编写自己的模块
# 1.模块就是程序,xx.py中xx就是模块名
# 2.模块通常用来下定义,即写通用方法,方便重用
# 3.使用模块时需要告诉解释器去哪里查找这个模块,在importModel中有说明
print('hello,this is my model')


def hello(s=''):
    print('这是函数方法')


def test():
    """测试方法"""
    hello()


if __name__ == '__main__':
    test()
