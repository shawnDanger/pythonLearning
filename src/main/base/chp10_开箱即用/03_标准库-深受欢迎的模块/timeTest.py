# time
import time

# 1.时间元组
# (tm_year=2018, tm_mon=12, tm_mday=5, tm_hour=19, tm_min=5, tm_sec=53, tm_wday=2, tm_yday=339, tm_isdst=0)最后一位是夏令时
secs = time.time()
tuples = time.localtime(secs)
print(tuples)
# 2.相互转换
#   1).元组转字符串
print(time.asctime())  # 转当前时间
strtime = time.asctime(tuples)
print('元组转字符串', strtime)
print('元组转格式化的字符串', time.strftime('%Y-%m-%d %H:%M%S', tuples))
#   2).秒转元组
print('秒转当地时间的日期元组', time.localtime(secs))
#   3).元组转秒
print('元组转秒', time.mktime(tuples))
#   4).字符串转元组
print('字符串转元组', time.strptime(strtime))
# todo datetime日期和时间算数支持
# todo timeit代码效率(计算代码执行时间)
