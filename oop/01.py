'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    pass

# 定义一个对象
mingyue = Student()

# 定义一个类，用来秒速听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进层级
    # 2. 系统默认有一个self参数
    def doHomework(self):
        print("我在做作业")

        # 推荐在函数末尾使用return语句
        return None
    def doHomeworks(self):
        print("My name is {0}".format(__class__.name))
        return None

yueyue = PythonStudent()
print(yueyue.__dict__)
yueyue.name = "yueyue"
yueyue.gender = "female"
print(yueyue.name)
print(yueyue.age)
print(yueyue.gender)
yueyue.doHomework()
print(yueyue.__dict__)
yueyue.doHomeworks()
