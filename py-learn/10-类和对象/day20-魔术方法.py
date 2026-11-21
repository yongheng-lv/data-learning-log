"""
魔术方法、封装
"""
# 魔术方法
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

# 封装:公开的成员方法访问私有成员方法
class Phone:    # 定义一个类，内含私有成员变量和私有成员方法
    __current_votage = 1    # 私有成员变量 无法直接访问
    def __keep_single_core(self):
        print("让CPU单核模式运行")
    def call_by_5G(self): # 定义一个公开成员方法，调用私有成员方法
        if self.__current_single_core >= 1:
            print("5G通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5G，以开启单核模式进行省电")
phone = Phone()
phone.call_by_5G