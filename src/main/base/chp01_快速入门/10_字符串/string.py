# 下面两种方式没有任何差别
print("这是字符串")
print('这也是字符串')

print("10.1 单引号字符串以及对引号转义")
print('"Let\'s go!",she said.')
print("\"Let\'s go!\",she said.")

print("10.2 拼接字符串")
a = "hello,"
b = ' world!'
print(a + b)

print("10.3 字符串表示str和repr")
print(repr("hello,\n world!"))
print(str("hello,\nworld!"))

print("10.4 长字符串,原始字符串和字节")
print("10.4.1 长字符串")
print("""
这是长字符串,
可以跨越多行,
也可以用三个单引号表示.
中间可以嵌入原始字符串,以此来避免使用"\\"
""")
print("常规字符串\
      如果要多行,在行未加'\\'\
      就可以多行,表达式和语句也适用.")

print("10.4.2 原始字符串")
print("会将转义字符串显示为原来的样子,结尾不能用'\\'")
print(r"若要使用转义可使用'转义符号',例" '\n' "就是这样")
print(r"Let's go!,\nshe said.")

print("10.4.3 Unicode、bytes和bytearray")
# todo 字符编码详解
