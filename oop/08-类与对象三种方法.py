class Animal():
    # 实例方法
    def eat(self):
        print("实例方法")

    # 类方法
    @classmethod
    def play(cls):
        print("类方法")

    # 静态方法
    @staticmethod
    def sleep():
        print("静态方法")


dog = Animal()
# 实例方法
dog.eat()
# 类方法
Animal.play()
dog.play()
# 静态方法
Animal.sleep()
dog.sleep()