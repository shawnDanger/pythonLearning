# 1.定义一个斐波那契函数
def fibs(num):
    '计算指定数量的斐波那契,此处单引号双引号均可'
    result = [0, 1]
    for i in range(num - 2):
        result.append(result[-2] + result[-1])
    return result


print(fibs(5))
# 2.并给其编写文档 :即在def下首行定义字符串
print(fibs.__doc__)
# 3.所有函数都期望有返回结果,但在python中,可能没有返回结果,此时会返回默认结果None
