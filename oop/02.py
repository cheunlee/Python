class A():
    name = "xiaoming"
    age = 18

    def __init__(self):
        self.name = "xiaohuang"
        self.age = 17

    def say(self):
        print("My name is {0}, and age is {1}".format(self.name,self.age))
        return None

class B():
    name = "xiaohong"
    age = 16

a = A()

a.say()
# 传入a
A.say(a)
# 传入类实例A
A.say(A)
# 传入类实例B
A.say(B)
# 鸭子模型

