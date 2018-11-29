# 导入模块的几种方法
import os
from os import _exists
from os import _exists, _add, _fspath, open
from os import *

# 第一种方法:不同模块直接模块名调用,不在演示
# 第二种方法:导入模块并起别名
os.open()
import os as os2

os2.open()
# 第三种方法:导入特定函数并起别名
from os import open as op

op()
"""
可以为模块起别名
也可以为特定函数起别名
"""
