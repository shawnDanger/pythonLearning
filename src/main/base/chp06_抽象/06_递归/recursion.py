# 有穷递归
# 也有无穷递归,但通常有穷是对我们有用的
"""
必要条件
1.基线条件(停止条件,出口)
2.递归条件
"""


def factorial(n):
    "阶乘"
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def power(x, n):
    '幂'
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


print(power(2, 3))


# todo 回头仔细核对,此方法有问题
def binarysearch(sequence, number, lower=0, upper=None):
    """二分查找,使用在非常大的数查找非常有用"""
    if upper is None: upper = len(sequence)
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return binarysearch(sequence, number, middle + 1, upper)
        else:
            return binarysearch(sequence, number, middle, upper)


se = [1, 2, 7, 4, 5, 6, 3, 8, 9]
# print(binarysearch(se, 3))
import bisect

print(bisect.bisect(se, 7))
"""
函数式编程!
但在python中通常使用类,推导,lambda表达式
"""
