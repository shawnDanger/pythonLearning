# 集合,堆和双端队列
# 1.集合 set是默认有的模块
#   1).创建  可使用序列或其他可迭代对象来创建集合,也可以通过{}来创建,但是不能创建空的set,否则会使字典

print(set(range(10)))
print(type({}))
print(type({1, 2}))
#   2).无序,去重
print({0, 1, 2, 1, 2, 3, 4})
#   3).计算
a = {1, 2, 3}
b = {2, 3, 4}
#       1).并集
print(a.union(b))
print(a | b)
#       2).交集
c = a & b
print(a, b, '交集', c)
print(a, b, '交集', a.intersection(b))
#       3).差集
print(a, b, '差集', a.difference(b))
print(a, b, '差集', a - b)
#       4).子集与父级
print(c, '是否是', a, '的子级', c.issubset(a), c <= a)
print(a, '是否是', c, '的父级', a.issuperset(c), a >= c)
#       5).相互差集的并集
print(a, b, '相互差集的并集', a.symmetric_difference(b))
print(a, b, '相互差集的并集', a ^ b)
#   4).实用
from functools import reduce

myset = []
for i in range(10):
    myset.append(set(range(i, i + 5)))
print(myset)
print(reduce(set.union, myset))
h = set({1, 2, 3})
i = set({2, 3, 4})
# print(h.add(i))  # 集合只能包含不可变(可散列)的值,因此不能包含其他集合
# print({1, 2, 3, {2, 3, 4}})
h.add(frozenset(i))  # frozenset表示不可变(可散列)的集合
print(h)  # todo 如何取到集合中集合的值,且此种方法集合值和集合中的集合的值可重复

# 2.堆(优先队列) heapq(q表示队列queue)需要导入此模块
from heapq import *
from random import shuffle

#   1).heappush添加
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap, n)
print('堆', heap)
# 元素排列顺序虽不严格排序,但必须保证位置i处的元数总是大于位置i // 2处的元素
# (也就是说小于位置2*i和2*i+1的元素),这是底层堆算法的基础,称为堆特征
heappush(heap, 0.5)
print('堆', heap)
#   2).heappop弹出最小元素(索引0)
heappop(heap)
print('弹出最小元素', heap)
#   3).heapify将列表变为合法的堆(使用最少的位移操作)
heapify(heap)
print('合法的堆', heap)
#   4).heapreplace弹出最小元素并压入新元素,效率比先弹出和压入块
heapreplace(heap, 11)
print('pop并push 11', heap)
heapreplace(heap, 10)
print('pop并push 10', heap)
#   5).nlargest(n,iter),nsmallest(n,iter)找出可迭代对象iter中最大和最小的n个元素
print('最大的两个:', nlargest(2, heap))
print('最小的两个:', nsmallest(2, heap))

# 3.双端队列(及其它集合),比集合弹出元素效率高
from collections import deque

q = deque(range(5))
print('初始双端队列', q)
q.append(5)
print('双端队列右追加', q)
q.appendleft(5)
print('双端队列左追加', q)
q.pop()
print('右弹出', q)
q.popleft()
print('左弹出', q)
q.rotate(2)  # todo 没搞明白怎么转的
print('旋转', q)
q.rotate(-2)
print('旋转', q)
