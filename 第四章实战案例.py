"""
练习案例：求1-100的和
需求：通过while循环，计算从1累加到100的和
提示：终止条件不要忘记，
设置为确保while循环100次
确保累加的数字，从1开始，到100结束
"""

# i = 1
# sum = 0
# while i <= 100:
#     sum += i
#     i += 1
# print(f"1到100的和是{sum}")

"""
设置一个范围1-100的随机整数变量，通过while循环，配合input语句，判断输入的数字是否等于随机数
• 无限次机会，直到猜中为止
• 每一次猜不中，会提示大了或小了
• 猜完数字后，提示猜了几次
• 提示：
• 无限次机会，终止条件不适合用数字累加来判断
• 可以考虑布尔类型本身（True or False）
• 需要提示儿次猜中，就需要提供数字累加功能
• 随机数可以使用：import random
num= random
"""

# import random
# num = random.randint(1,100)
# count = 0
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜的数字："))
#     count += 1
#     if guess_num == num:
#         print("猜中了")
#         flag = False
#     else:
#         if guess_num > num:
#             print("猜大了，再猜一次：")
#         else:
#             print("猜小了，再猜一次：")
# print(f"你一共猜了{count}次")

"""
输出九九乘法表
"""

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j}*{i} = {j * i}\t",end='')
#         j += 1
#     i += 1
#     print() # 空内容，输出换行

"""
练习案例：数一数有几个o
定义字符串变量name，内容为："lvyongheng is a good boy"
通过for循环，遍历此字符串，统计有多少个英文字母："o"
lvyongheng is a good boy中共含有：4个字母o
提示：
1. 计数可以在循环外定义一个整数类型变量用来做累加计数
2. 判断是否为字母"a”，可以通过if语句结合比较运算符来完成
"""
# name = "lvyongheng is a good boy"
# sum = 0
# for x in name:
#     if x == "o":
#         sum += 1
# print(f"这串代码共有{sum}个o")

"""
定义一个数字变量num，内容随意
并使用range（）语句，获取从1到num的序列，使用for循环遍历它。
在遍历的过程中，统计有多少偶数出现
"""
# num = 1314
# count = 0
# for i in range(1315):
#     if i % 2 == 0:
#         count += 1
# print(f"从1到1315共有{count}个偶数")

"""
通过for循环，输出如下九九乘法表内容
"""
# for i in range(1,10):
#     for j in range(1,i + 1):
#         print(f"{i} * {j} = {j * i}\t",end='')
#     print()

"""
某公司，账户余额有1W元，给20名员工发工资。
 员工编号从1到20，从编号1开始，依次领取工资，每人可领取1000元
 领工资时，财务判断员工的绩效分（1-10）（随机生成），如果低于5，不发工资，换下一位
如果工资发完了，结束发工资。
 使用循环对员工依次发放工资

 提示：continue用于跳过员工，break直接结束发工资
 随机数可以用：
 import random
num = random.randint（1, 10）
"""
import random
num = random.randint(1,10)
total_wage = 10000
for i in range(1,21):
    if num >= 5:
        print(f"第{i}号发1000元工资")
    else:
        print("绩效不合格，不发工资")
    continue
    total_wage -= 1000