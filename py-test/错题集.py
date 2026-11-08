"""
通过for循环，输出如下九九乘法表内容
"""
# for i in range(1,10):
#     for j in range(1,i + 1): 
#         print(f"{i} * {j} = {i * j}\t",end='')
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
# money = 10000
# for i in range(1,21):
#     import random
#     num = random.randint(1,10)
#     if num < 5:
#         print(f"第{i}号绩效不合格，不发")
#         continue
#     else:
#         if money >= 1000:
#             money -= 1000
#             print(f"第{i}号绩效合格，发放1000元")
#         else:
#             print("总资金不足，不再发放，请下个月再来")
#             break

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
num= random.randint(1,100)
"""
import random
num = random.randint(1,100)
count = 0
while True:
    guess_num = int(input("请输入你猜的数字："))
    count += 1
    if guess_num > num:
        print("大了，继续猜：")
    elif guess_num < num:
        print("小了，继续猜：")
        continue
    else:
        print(f"恭喜，第{count}次猜中了{num}")
        break