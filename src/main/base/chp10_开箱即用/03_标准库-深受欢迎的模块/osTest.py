import os
from pprint import pprint

print(os.__all__)
# 1.一些属性
pprint(os.environ)  # 包含环境变量的映射
print(os.sep)  # 路径名的分隔符
print(os.pathsep)  # 路径分隔符
pprint(os.linesep)  # 行分隔符
print(os.urandom(12))  # 随机强加密

# 2.运行外部程序(有种会在本地留下缓存)
# pprint(os.system('sysTest.py'))  # 运行外部程序(退出python解释器,控制权给外部程序),execv,popen也可以(创建一个到程序的连接,类似于文件),startfile更优打开方案
# os.execv('XMind.exe',['python','sysTest','method'])  # todo 如何使用
# os.popen('XMind.exe')
# print(os.system('D:\MajorSoftware\Sublime Text 3\sublime_text.exe'))
# print(os.system('D:\"MajorSoftware"\"Sublime Text 3"\sublime_text.exe'))  # 必须加上""而且必须关闭当前窗口,但是有问题

#   1).适合直接启动文件
# print(os.startfile('D:\MajorSoftware\Sublime Text 3\sublime_text.exe'))  # 直接写路径即可运行
# print(os.startfile(r'D:\MajorSoftware\截图工具\FSCapture\FSCapture.exe'))
# print(os.startfile('xmind.exe'))  # 或者直接在path路径下存在的也可以运行

# subprocess 融合上述三种方式(不包括startfile,webbrowser)
import subprocess
# subprocess.Popen('XMind.exe')

#   2).适合直接启动浏览器
import webbrowser
# webbrowser.open('http://www.python.org')
