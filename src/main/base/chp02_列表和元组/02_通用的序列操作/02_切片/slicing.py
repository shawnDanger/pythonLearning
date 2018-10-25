# 第一个索引时包含的第一个元素的编号,第二个索引时切片后余下的第一个元素的编号
link = '<a href="http://www.python.org">Python web site</a>'
print(link[9:30])
print(link[32:-4])

print('2.1 绝妙的简写')
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 超出列表范围
print(nums[7:9])  # 索引不全
print(nums[7:10])  # 访问最后一位需要达到最长长度加一
print(nums[7:])  # 或者最后一位不写可以访问全部
# 负数索引
print(nums[-3:-1])
print(nums[-3:0])
print(nums[-3:])
print(nums[:3])
# 全列表
print(nums[:])

print('2.2 更大的步长')
# print(nums[0:10:0])步长为零则无法移动,会报错
print(nums[0:10:1])
print(nums[1:10:2])
print(nums[::2])
print(nums[::-1])
print(nums[::-2])
