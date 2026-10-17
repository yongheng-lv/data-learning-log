"""布尔数据类型-if基础
"""

# 定义数据变量存储布尔数据
bool_1 = True
bool_2 = False
print(f"bool_1的数据变量内容是{bool_1},数据类型是{type(bool_1)}")
print(f"bool_2的数据变量内容是{bool_2},数据类型是{type(bool_2)}")
# 比较运算符的使用
num1 = 5
num2 = 7
print(f"5 == 7的结果是{num1 == num2}")
print(f"5 != 7的结果是{num1 != num2}")
# print("5 == 7的结果是",num1 == num2)

# if语句基本格式
age = 20
if age >= 18:
    print("我已经成年了，即将步入大学生活")
# 小测
age = input("请输入你的年龄:")
age_num = int("age")
if age_num >= 18:
    print("您已成年,请补票10元")