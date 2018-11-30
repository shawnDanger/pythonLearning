# 两个变量都指向这个列表地址,列表一改所有都改
names = ['Mr.Entity', 'Mr.Shawn']
n = names
n[0] = 'Mr.Deng'
print(names)
# 避免以上情况,可创建副本
# 使用切片创建副本
names = ['Mr.Entity', 'Mr.Shawn']
n = names[:]
print(n is names)
print(n == names)
