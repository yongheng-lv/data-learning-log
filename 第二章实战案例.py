"""
1.定义一个变量，数字类型，内容随意。
2.基于input语句输入猜想的数字，通过if和多次elif的组合，判断猜想数字是否和心里数字一致
"""
num = 10
if int(input("猜猜我想的数字是几：")) == num:
    print("恭喜猜对啦")
elif int(input("不对，再猜一次：")) == num:
    print("恭喜猜对啦")
else:
    print("都不对，我猜的是：10")

"""
案例需求：
定义一个数字（1~10，随机产生），通过3次判断来猜出来数字
案例要求：
1.数字随机产生，范围1-10
2.有3次机会猜测数字，通过3层嵌套判断实现
3.每次猜不中，会提示天了或小了
提示，通过如下代码，可以定义一个变量num，变量内存储随机数字。
import random
num = random.randint（1, 10）
"""
import random
num = random.randint(1,10)
if int(input("请输入数字")) > num:
    print("你猜大了，请再猜一次")
    if int(input("请输入数字：")) < num:
        print("你猜小了，请再猜一次")