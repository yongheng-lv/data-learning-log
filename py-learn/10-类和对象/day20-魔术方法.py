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
    def __lt__(self, other):
        return self.age < other.age
    def __le__(self, other):
        return self.age <= other.age
    def __eq__(self, other):
        return self.age == other.age
stu1 = Student("蔡徐坤", 21)
stu2 = Student("周杰轮", 22)
print(str(stu1))
print(stu1 < stu2)
print(stu1 <= stu2)
print(stu2 >= stu1)
print(stu1 == stu2)