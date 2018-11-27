from math import pi

# 填充0
print('{:010.2f}.'.format(pi))
# 填充格式:左对齐<,居中^,右对齐>
print('{0:<10.2f}.\n{0:^10.2f}.\n{0:>10.2f}.\n'.format(pi))
# 填充字符扩展对齐说明符
print('{:#^15}'.format(' WIN BIG '))
# 更具体的说明符=,指定将填充字符放在符号和数字之间
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi))
print('{0:10.2f}\n{1:=10.2f}'.format(pi, -pi))
# 正数加上符号,可以使用说明符+(对齐说明符后面),默认符号为-,如果符号说明符指定为空格,会在正数前面加上空格而不是+
print('{0:-.2}\n{1:-.2}'.format(pi, -pi))  # 默认设置
print('{0:+.2}\n{1:.2}'.format(pi, -pi))
print('{0: .2}\n{1: .2}'.format(pi, -pi))
# 放在符号说明符和宽度之间,作用是触发另一种转换方式,转换细节随类型而异
print('{:b}'.format(42))
print('{:#b}'.format(42))
print('{:g}'.format(42))
print('{:#g}'.format(42))
