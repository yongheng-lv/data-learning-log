"""
魔术方法、封装
"""
class Student:
    name = None
    age = None
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"这名练习生叫{self.name}，年龄是{self.age}"
stu = Student("蔡徐坤", 21)
print(str(stu))
