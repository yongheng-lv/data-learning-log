"""
开学了有一批学生信息需要录入系统，请设计一个类，记录学生的：
姓名、年龄、地址，这3类信息
请实现：
通过for循环，配合input输入语句，并使用构造方法，完成学生信息的键盘录入
输入完成后，使用print语句，完成信息的输出

当前录入第1位学生信息，总共需录入10位学生信息
请输入学生姓名：周杰轮
请输入学生年龄：31
请输入学生地址：北京
学生1信息录入完成，信息为：【学生姓名：周杰轮，年龄：31，地址：北京】
当前录入第2位学生信息，总共需录入10位学生信息
请输入学生姓名：
"""
class Student:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.addr = addr
for i in range(1, 2):
    print(f"当前录入第{i}位学生信息，总共需录入10位学生信息")
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    addr = input("请输入学生住址：")
    stu = Student(name, age, addr)
    print(f"学生{i}信息录入完成，信息为：【学生姓名：{stu.name}，年龄：{stu.age}，地址：{stu.addr}】")

"""
设计一个手机类，内部包含：
• 私有成员变量：
__is_5g_enable，类型bool，True表示开启5g，False表示关闭5g
• 私有成员方法：
__check_5g（），会判断私有成员__is_5g_enable的值
• 若为True，
打印输出：5g开启
• 若为False，
打印输出：5g关闭，使用4g网络
公开成员方法：call_by_5g（），调用它会执行
• 调用私有成员方法：__check_5g（），判断5g网络状态
• 打印输出：正在通话中
运行结果：5g关闭，使用4g网络
正在通话中
"""
class Phone:
    __is_5G_enable = False
    def __check_5G(self):
        if self.__is_5G_enable:
            print("5G开启")
        else:
            print("5G关闭，使用4G网络")
    def call_by_5G(self):
        self.__check_5G()
        print("正在通话中")
phone = Phone()
phone.call_by_5G()