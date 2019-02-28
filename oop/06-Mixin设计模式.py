class Person():
    def __init__(self):
        pass
    def sleep(self):
        print("Sleep ...")

class Teacher(Person):
    def __init__(self):
        pass
    def teach(self):
        print("Teach ...")

class Student(Person):
    def __init__(self):
        pass
    def study(self):
        print("Study ...")

class Tutor(Teacher,Student):
    pass

t = Tutor()
print(Tutor.__mro__)