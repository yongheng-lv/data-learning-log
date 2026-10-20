"""
通过for循环，输出如下九九乘法表内容
"""
for i in range(1,10):
    for j in range(1,i + 1): 
        print(f"{i} * {j} = {i * j}\t",end='')
    print()

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
money = 10000
for i in range(1,21):
    import random
    num = random.randint(1,10)
    if num < 5:
        print(f"第{i}号绩效不合格，不发")
        continue
    else:
        if money >= 1000:
            money -= 1000
            print(f"第{i}号绩效合格，发放1000元")
        else:
            print("总资金不足，不再发放，请下个月再来")
            break