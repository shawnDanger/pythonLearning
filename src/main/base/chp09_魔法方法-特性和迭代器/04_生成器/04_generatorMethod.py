# 生成器的方法
# send,throw,close
"""
在生成器开始运行之后,可以使用生成器和外部之间和通信渠道向他提供值,通信渠道包含如下两个端点:
  1.外部世界:外部世界可访问生成器的方法send,类似于next,但接受一个参数(任何对象)
  2.生成器:在挂起的生成器内部,yield可能用作表达式而不是语句.
    换言之,当生成器重新运行时,yield返回一个值,通过send从外部世界发送的值.如果使用的是next,yield将返回None
请注意:仅当生成器被挂起(即遇到第一个yield)后,使用send(而不是next)才有意义.要再此之前向生成器提供信息,可使用生成器函数的参数
如果一定要在生成器刚启动是对其调用方法send,可向它传递参数None
"""
import sys


def repeater(value):
    while True:
        new = (yield value)  # 并非必须这样做,但如果要以某总方式使用返回值,尽管括起来
        if new is not None: value = new


r = repeater(23)
# r = repeater(None)  # 如果一定要在生成器刚启动是对其调用方法send,可向它传递参数None
print(next(r))
print(next(r))
r.send("hello")
print(next(r))
# 停止生成器
# r.close()
# print(next(r))
# 用于在yield中引发异常
# r.throw(Exception, '抛出异常', None)
