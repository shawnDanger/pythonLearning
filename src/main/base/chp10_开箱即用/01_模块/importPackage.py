import package, sys, pprint

pprint.pprint(sys.path)
print(package.PI)  # 可用__init__中的变量,函数
print(package.math.sqrt(4))  # 可用__init__中导入的包的变量,函数

import package.colors

package.colors.blue()  # 变量名必须是package.colors

from package import shapes

shapes.sq()
