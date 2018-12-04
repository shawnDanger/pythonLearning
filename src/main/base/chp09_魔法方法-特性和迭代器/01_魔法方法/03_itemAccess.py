# 元素访问
# 本节介绍的魔法方法能够创建行为类似于序列或映射的对象
# 要实现基本的序列和映射协议(接口)非常简单
# 序列和映射都是元素(item)的集合,要实现他们的基本行为(协议),不可变对象实现2个方法,可变对象需要实现4个
# 例1.无穷序列(基于手动实现)


def check_index(key):
    """
    指定的键是否是可接受的索引
    :param key: 键值
    :return:
    """
    if not isinstance(key, int): raise TypeError
    if key < 0: raise IndexError


class ArithmeticSequence:
    """
    算术序列
    """

    def __init__(self, start=0, step=1):
        """
        :param start: 第一个值
        :param step: 两个相邻的值
        :param changed: 一个字典,包含用户修改后的值
        """
        self.start = start
        self.step = step
        self.changed = {}

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step

    def __setitem__(self, key, value):
        check_index(key)
        self.changed[key] = value
    # def __del__(self):
    #     """删除方法,此处禁止,不需要实现"""
    #     pass
    # def __len__(self):
    #     """长度,不实现则无限长"""
    #     pass


s = ArithmeticSequence(1, 2)

print(s[4])


# 例2:访问计数器(派生,继承)
class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.count = 0

    def __getitem__(self, index):
        self.count += 1
        return super(CounterList, self).__getitem__(index)


cl = CounterList(range(10))
print(cl)
cl.reverse()
print(cl)
del cl[1:3]
print(cl)

"""
更多魔法方法参见Python Reference Manual的Sepecial method names
"""
