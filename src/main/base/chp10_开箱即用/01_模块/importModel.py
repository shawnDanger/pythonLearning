# 1.告诉解释器在哪里查找模块,或者直接将模块放在sys.path目录下,或者在环境变量里添加python路径
import sys, pprint

# sys.path.append('D:\\MajorSoftware\\IDEA\\PyCharm\\PyCharmWorkspace\\GitHub\\pythonLearning\\src\\main\\base\\chp10_开箱即用\\01_模块')  # 临时加入
# sys.path.remove('D:\\MajorSoftware\\IDEA\\PyCharm\\PyCharmWorkspace\\GitHub\\pythonLearning\\src\\main\\base\\chp10_开箱即用\\01_模块')
pprint.pprint(sys.path)

# 2.导入自定义模块
import model  # 仅在第一次导入时执行print

#   导入多次和只导入一次效果相同,是一种优化
model.hello()
#   为何pycharm语法检查报错但仍能正确执行,因为sys.path中已含有此路径,若删除此路径,则找不到此模块

# 3.重新导入模块
import importlib

importlib.reload(model)

# 4.命令行执行程序
#   让程序可用后(像处理模块那样),可用python解释器开关-m来执行它
# 如果随其他模块一起安装了文件progname.py
# python -m progname args将使用args来执行程序progname

# 5.模块中的测试代码,参见model中test()函数
# print(model.__name__)
model.test()
