class Person():
    name = None
    __age = 10
    gender = "female"
    _nickname = "goudan"

    def sleep(self):
        if self.gender == "female":
            print("she is sleeping")
        else:
            print("he is sleeping")
        return None

# 继承
# 父类写在括号内
class Teacher(Person):
    teacher_id = "9277"
    def make_exam(self):
        print("teacher is making exam")
        return None

class Student(Person):
    score = 90
    def test(self):
        if self.score >= 90:
            print("A")
        else:
            print("OK")
    def sleep(self):
        #Person.sleep(self)
        super().sleep()
        self.test()
# 子类父类定义同名变量，访问时就近原则

s = Student()
s.sleep()
