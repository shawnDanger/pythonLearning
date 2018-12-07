#!D:\Program Files\Python3.6\python.exe
from setuptools import setup

# 1.安装
# setup(name='Hi',
#       version='1.0.0',
#       description='一个简单样例',
#       author='shawn dang',
#       requires=['hi'])
# 执行python setup.py install命令安装
# 2.打包
# 获取打包帮助python setup.py sdist --help-formats
# 执行python setup.py sdist --formats=zip,gztar
# 3.编译扩展 需要语言的源代码...
# from setuptools import Extension
#
# setup(name='hi',
#       version='1.0',
#       ext_modules=[Extension('hi', ['hi2.c'])])
# 4.使用pyinstaller创建可执行程序exe(直接执行pyinstaller -F hi.py(文件名))
# py2exe已经过时,是py2.x用的版本
