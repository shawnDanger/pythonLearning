# re:正则表达式的支持(重点)
import re

print('python正则学习资料', 'https://docs.python.org/3/howto/regex.html')
# todo 一.正则表达式是什么
# 二.模块re内容-重要函数
# 1.compile 用字符串表示的正则表达式转换为模式对象,提高匹配效率
# 2.search 在给定字符串中查找第一个域指定正则表达式匹配的子串
if re.search('.ython', 'www.python.org'):
    print('find python')
# 3.match 尝试在给定str开头(重点,即以xxx开头)查找与正则表达式匹配的子串
print(re.match('p', 'python'))
# 4.split 根据模式匹配的子串来分割字符串
text = 'alpha,beta,,,gamma  delta'
print(re.split('[, ]+', text))
# 5.findall 返回一个列表,包含所有与给定模式匹配的子串
findallstr = 'Hi!aym...are you sure?sure.'
print('查找所有单词', re.findall('[a-zA-Z]+', findallstr))
print('查找所有符号', re.findall('[.?!\-,]+', findallstr))
# 6.sub 从左往右将与模式匹配的子串替换为指定内容
print(re.sub('{name}', 'shawn', 'Dear {name}...'))
print(re.sub('name', 'shawn', 'Dear name...'))
# 7.escape 工具函数,用于对字符串中所有可能被视为正则表达式运算符的字符进行转移.
print(re.escape('www.python.org'))
print(re.escape('But where is the ambiguity?'))
# 有些函数参数有flags,可用于修改正则的解读方式

# 三.模块re内容-匹配对象和编组(编组使用'()')
m = re.match('www\.(.*)\..{3}', 'www.python.org')
print(m.group(0))  # 返回与模式中给定编组匹配的子串(编组号默认为0)
print(m.group(1))
print(m.start(1))  # 返回给定编组匹配的子串的起始索引
print(m.end(1))  # 类似start,但返回终止索引+1
print(m.span(1))  # 返回一个元组,其中包含与给定编组匹配的子串起始索引和终止索引

# 四.模块re内容-替换中的组号和函数
# emphasis_pattern = r'\*([^\*]+)\*'  # 同下一样
emphasis_pattern = re.compile(r'''
\*          # 起始突出标志-一个*
(           # 与要突出的内容匹配的编组的起始位置
[^\*]+      # 与除*外的其他字符都匹配
)           # 编组到此结束
\*          # 结束突出标志
''', re.VERBOSE)  # 使用VERBOSE后可以在模式中添加空白(空格,制表符,换行符)
#   sub的强大功能               此处\1是编组1
repl = r'<em>\1</em>'
str = '*Hello*, *world*!'
print(re.sub(emphasis_pattern, repl, str))
# 重复运算符默认是贪婪的,需要在运算符后加?才为非贪婪模式,如下
emphasis_pattern = r'\*(.+)\*'
print('贪婪模式:', re.sub(emphasis_pattern, repl, str))
emphasis_pattern = r'\*(.+?)\*'
print('非贪婪模式:', re.sub(emphasis_pattern, repl, str))
# 例子:模板系统匹配[x=1]+[y=2]=[x+y]替换值,使用eval计算表达式,否则返回''
