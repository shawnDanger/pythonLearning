# 替换字段名
# 混合使用,注意带有key的没有索引,不带key的成一个序列,有索引

# 索引顺序匹配  自动编号
s1 = '{foo} {} {bar} {}'.format(1, 2, bar=4, foo=3)
print(s1)
# 指定索引匹配  手动编号
s2 = '{foo} {1} {bar} {0}'.format(1, 2, bar=4, foo=3)
print(s2)

# 提供其组成部分,列表,元组等
# 列表
fullname = ['Alfred', 'Smoketoomuch']
s3 = 'Mr {name[1]}.'.format(name=fullname)
print(s3)

# 句点访问模块中方法,属性,变量和函数
import math

s4 = 'The {module.__name__} module defines the value {module.pi} for π.'.format(module=math)
print(s4)
