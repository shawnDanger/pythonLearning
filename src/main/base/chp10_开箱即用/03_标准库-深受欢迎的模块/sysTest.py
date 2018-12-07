import sys
from pprint import pprint

pprint(sys.argv)  # 接受命令行运行python的参数
pprint(sys.modules)  # 将模块名映射到模块(仅限当前导入的模块)
pprint(sys.path)  # import在这些目录中查找模块
pprint(sys.platform)  # 平台信息
print(sys.stdout)  # 标准输出流
print(sys.stdin)  # 标准输入流
print(sys.stderr)  # 标准错误流
print(help(sys))
