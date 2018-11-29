# 跳出循环
# break
for n in range(0, 10):
    if n == 5: break
    print(n)
# continue
for n in range(0, 10):
    if 3 <= n <= 5: continue
    print(n)
# 判断循环结束,仅在没有执行break是执行else
print("break")
for n in range(0, 10):
    if n == 5: print('this is ', n)
    print(n)
else:
    print('for is break')
