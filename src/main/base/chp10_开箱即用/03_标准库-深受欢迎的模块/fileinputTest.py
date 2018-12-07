# -*- coding: utf-8 -*-
# 迭代一系列文本文件中的所有行
import fileinput as fi

# 返回可在for循环中进行迭代的对象
for f in fi.input():  # 务必测试正确之后使用inplace,否则会破坏文件.不使用时会打印结果,并不修改源文件
    f = f.rstrip()  # 指定删除两端空白并返回结果
    # fi.nextfile()  # 关闭当前文件并移到下一个文件
    print('{:<50} # {:2d}'.format(f, fi.filelineno()),  # 跨文件行号
          fi.filename(),  # 文件名称
          fi.lineno(),  # 文件行号
          fi.isfirstline()  # 是否是第一行
          )
# 编写好后在终端执行python fileinputTest.py file1.py file2.py等n个文件名
# fi.isstdin()  # 检查最后一行是否来自sys.stdin
# fi.close()  # 关闭序列
