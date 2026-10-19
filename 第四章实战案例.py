"""
练习案例：求1-100的和
需求：通过while循环，计算从1累加到100的和
提示：终止条件不要忘记，
设置为确保while循环100次
确保累加的数字，从1开始，到100结束
"""
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"1到100的和是{sum}")

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
import random
num = random.randint(1,100)
count = 0
flag = True
while flag:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num == num:
        print("猜中了")
        flag = False
    else:
        if guess_num > num:
            print("猜大了，再猜一次：")
        else:
            print("猜小了，再猜一次：")
print(f"你一共猜了{count}次")

"""
输出九九乘法表
"""