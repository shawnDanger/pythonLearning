# 简单模拟大部分生成器
# yield some_expression 替换如下:
# result.append(some_expression)
# 末尾加上return result


def flatten(nested):
    result = []
    try:
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:
            for element in flatten(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


print(flatten(['abb', ['bcc', ['cdd']]]))
