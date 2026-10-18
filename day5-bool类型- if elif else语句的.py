"""布尔数据类型-if else基础
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
age = input("欢迎来到黑马游乐园,儿童免费,成人收费,请输入你的年龄:")
age = int(age)
if age >= 18:
    print("您已成年,请补票10元")
    print("祝您游玩愉快")
# if else
high = 170
if high >= 150:
    print("您需购票")
else:
    print("您可以免费游玩")
# 小测
high = int(input("请输入您的身高："))
if high > 130:
    print("您需补票10元")
else:
    print("您可以免费游玩")
# if elif else
vip_level = int(input("请输入VIP等级："))
high = int(input("请输入身高："))
day = int(input("请输入今天的日期："))
if vip_level >3:
    print("您的VIP级别>3，免费玩")
elif high < 130:
    print("您的身高不足130，免费玩")
elif day == 1:
    print("今天是1号，免费玩")
else:
    print("您不满足免费游玩的条件，请补票")