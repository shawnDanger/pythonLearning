# 1.center 默认两天填充空格

world = 'The Middle by Jimmy Eat World'
print(world.center(39))
print(world.center(39, '*'))

# 2.find 在字符串查找子串,如果找到就返回第一个字符串的索引,否则返回-1
print('The Middle by Jimmy Eat World Eating'.find('Eat'))
print('The Middle by Jimmy Eat World Eating'.find('eat'))
print('The Middle by Jimmy Eat World Eating'.find('Eat', -7, -1))  # 指定搜索起点和终点

# 3.join 合并序列的元素,与split作用相反,只可以合并字符串
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))  # 合并字符串元素
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
# 4.lower 返回字符串小写版本
print(world.lower())
# 所有单词首字母大写
print(world.title())
# 所有单词首字母大写
import string

print(string.capwords(world))
# 5.replace 指定字符串都替换为另一个字符串,并返回替换后结果
print(world.replace('Middle', 'Small'))
# 6.split 用于将字符串拆分为序列
print('1,2,3,4,5'.split(','))
print('1 2 3\n4 5   6'.split())
# 7.strip 将字符串开头和末尾(不含中间)的空白删除,返回删除后的结果
stripStr = '  *** select * from everyone!!! ***  '
print(stripStr.strip())
print(stripStr.strip('!* '))
# 8.translate与replace一样替换字符串特定部分,但其可以替换多个字符
# 这是利用Unicode码点之间的转换,第三个参数是删除哪些字符
maketrans = str.maketrans('cs', 'zf', '! ')
print(maketrans)
s = 'this is my favorite cs!'
print(s.translate(maketrans))
# 9.判断字符串是否符合特定的条件(许多is开头的方法)
print(s.islower())
