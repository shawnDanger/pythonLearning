# 递归式生成器
def flatten(nested):
    try:
        # 不迭代类似于字符串的对象
        # try:
        #     nested + ''  # 此处没有执行类型检查!只是检查行为.一种更自然的替代方案是使用isinstance以及字符串和类似于字符串的一些抽象超类,但没有这样的类(3.5)
        #     print(isinstance(nested,str))
        # except TypeError:
        #     pass
        # else: raise TypeError
        if isinstance(nested, str):  # 3.6已出str的类型检查
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                yield element
    except TypeError:
        yield nested


print(list(flatten(['foo', ['bar', ['baz']]])))
