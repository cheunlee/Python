class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.setName(name)
    def intro(self):
        print("Hi, my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()


# property案例
class Animal():
    def fget(self):
        return self._name * 2
    def fset(self,name):
        self._name = name.upper()
    def fdel(self):
        self._name = "NoName"
    name = property(fget,fset,fdel,"update")

    def __call__(self, *args, **kwargs):
        return "bbbb"
    def __str__(self):
        return "aaaa"

a = Animal()
# 对象当函数使用时，要定义__call__
a()
# 当对象当做字符串使用时候，要定义__str__
print(a)


class A():
    name = "aaa"
    def __getattr__(self, item):
        print(item)
    def __setattr__(self, key, value):
        print(key,value)
        # 死循环
        #self.key = value
        super().__setattr__(key,value)
    def __delattr__(self, item):
        print(item)
    def __gt__(self, other):
        return self.name > other.name
a = A()
print(a.name)
print(a.age)
a.name = "vvv"
a.age = 19
print(a.__dict__)
b = A()
b.name = "zzz"
print(a > b)

