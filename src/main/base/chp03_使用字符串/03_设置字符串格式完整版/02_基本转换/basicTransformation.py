# 基本转换,指定要在字段包含的值后,就可以设置其格式的指令
# 转换标志'!'
print('{pi!s},{pi!r},{pi!a}'.format(pi='π'))

# 格式说明符号':'
print('The Number is {num}'.format(num=20))
print('The Number is {num:f}'.format(num=20))
print('The Number is {num:.2f}'.format(num=20))
print('The Number is {num:b}'.format(num=20))

"""
!后指令
s str
r repr
a ascii

:后说明符
b 将证书表示为二进制数
c 将整数解读为Unicode码点
d 整数视为十进制数处理
e 使用科学表示法来表示小数
E 与e相同,但使用E来表示指数
f 将小数表示为定点数
F 与f相同,但对于特殊值(nan和inf),使用大写表示
g 自动在定点表示法和科学表示法作出选择,这是默认用于小数的说明符,但在默认情况下至少有一位小数
G 与g相同,但使用大写来表示指数和特殊值
n 与g相同,但插入随区域而异的数字分割符
o 将证书表示为八进制数
s 保持字符串的格式不变,这是默认用于字符串的说明符
x 将整数表示为十六进制并使用小写字母
X 与x相同,但使用大写字母
% 将数表示为百分比值(乘以100,按说明符f设置格式,再在后面加上'%')
"""
