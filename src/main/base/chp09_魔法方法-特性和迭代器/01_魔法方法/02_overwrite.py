# 重写普通方法和特殊的构造函数
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('吃...')
            self.hungry = False
        else:
            print('No,thanks!')

    def sing(self):
        print('叽叽喳喳')


class SongBird(Bird):
    def __init__(self):
        """重写特殊的构造函数"""
        # 1.调用未关联的超类构造函数
        # Bird.__init__(self)  # 通常方法的self将自动关联到实例,但此处你可以随便设置参数self,这样的方法称为未关联的
        # 2.使用super函数
        super().__init__()
        self.sound = 'Squawk!'

    def sing(self):
        """重写普通方法"""
        print(self.sound)


# 重写构造函数会造成如下情况,没有父类构造定义的属性,解决方法如有两种:
# 1.调用未关联的超类构造函数(旧版本)
# 2.使用函数super(新版本,推荐使用)
sb = SongBird()
sb.eat()
