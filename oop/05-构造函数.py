class Animal():
    pass
class PanXingAnimal(Animal):
    def __init__(self,name):
        print("PanXing init ...name is {0}".format(name))
class Dog(PanXingAnimal):
    # __init__ 就是构造函数
    # 每次实例化的时候，第一个被调用
    # 主要工作是初始化
    def __init__(self):
        print("init ...")

#kaka = Dog()

class Cat(PanXingAnimal):
    pass

c = Cat("kaka")