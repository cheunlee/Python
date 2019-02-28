class Person():
    # 公有变量
    name = "xiaohuang"
    # 私有变量
    __age = 18

p = Person()
# 访问公有变量
print(p.name)
# 查看类的成员
print(Person.__dict__)
# 私有变量的访问，虽然能访问，但是作者既然写保护则不推荐访问和修改
p._Person__age = 19
print(p._Person__age)