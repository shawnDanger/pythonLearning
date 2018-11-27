# 设置字符串格式精简版
# %s为转换说明符,指出要将值插入到什么地方,s将值设置为字符串进行格式设置
format = 'Hello, %s. %s enough for ya?'
vars = ('world', 'Hot')
result = format % vars
print(result)

# 类的方法
from string import Template

tmpl = Template('Hello, $who! $what enough for ya?')
str = tmpl.substitute(who='shawn', what='Dusty')
print(str)

# 默认序列
s1 = '{},{} and {}'.format('first', 'two', 'three')
print(s1)

# 带索引
s2 = '{0} {1} {2} {3} {0} {1}'.format('to', 'be', 'or', 'not')
print(s2)

# 可设置值类型
from math import pi

s3 = '{name} is approximately {value:.10f}.'.format(value=pi, name='π')
print(s3)

# 3.6新特性
from math import e

s4 = f"Euler's constant is roughly {e}"
print(s4)
