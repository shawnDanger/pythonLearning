# todo 列表方法
a = [1, 2, 3]

print('1 append')
a.append(4)
print(a)

print('2 clear')
b = [1, 2]
b.clear()
print(b)

print('3 copy')
# 与a[:]和list(a)一样,都是复制
b = a.copy()
b[2] = 4
print('复制后b改动:' + str(b))
print('b改动后a:' + str(a))

print('4 count')
print('b:' + str(b))
print('统计b中出现4的次数:' + str(b.count(4)))
print('5 extend')
# 会修改原列表
a.extend(b)
print('a.extend(b)后a:' + str(a))
# 不会修改原列表
c = a + b
print('a+b后a:' + str(a))
print('6 index')
print(a.index(3))
# 不存在时会报错
# print(b.index(3))
print('7 insert')
a.insert(4, '5')
print(a)
print('8 pop')
# 弹出指定索引元素,弹出返回值为该元素
a.pop(4)
print(a)
# 弹出最后一位索引元素
a.pop()
print(a)
print('9 remove')
# 删除第一个指定值的元素
a.remove(4)
print(a)
print('10 reverse')
print('相反顺序排列前:' + str(a))
a.reverse()
print('相反顺序排列后:' + str(a))
a.__reversed__()
print('相反顺序排列后:' + str(a))
print('11 sort')
# 直接修改a,没有返回值
a.sort()
print(a)
print('12 sort->key,reverse')
a[-1] = 44
# 逆序排序
a.sort(reverse=True)
print(a)
d = sorted('python')
print(c)
d.insert(0, 'th')
# 按长度排序
d.sort(key=len)
print(d)
