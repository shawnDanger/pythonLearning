# 发出警告
from warnings import warn

warn('我感觉此处有点糟')
# 过滤警告
from warnings import filterwarnings

filterwarnings('ignore')
warn('有人在么')
# filterwarnings('error')  # 可以将警告引发成异常,但必须是Warning的子类
warn('有点糟')
# 过滤特定类型的警告
# filterwarnings('error')
warn('什么鬼', DeprecationWarning)  # 引发指定警告类型的异常

filterwarnings('ignore', category=DeprecationWarning)
warn('特殊类型', DeprecationWarning)
warn('特殊类型已被过滤,我不是特殊类型')
# todo warnings高级功能再补充
