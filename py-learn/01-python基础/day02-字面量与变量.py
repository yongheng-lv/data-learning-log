"""
本代码演示了：
-各类字面量的写法
-通过print语句输出各类字面量
"""
# 写一个整数字面量
666
# 写一个浮点数字面量
13.14
# 写一个字符串字面量
"黑马程序员"
# 通过print语句输出各类字面量
print("黑马程序员")
print(666)
print(13.14)
"""
演示python中变量的使用
"""
# 定义一个变量使其表示钱包的余额
money = 50
# 通过print语句·输出钱包的余额
print("钱包的余额为：", money)
# 买了一个冰激凌，花费10元
money = money - 10
# 通过print语句输出买冰激凌后的余额
print("买了一个冰激凌后，钱包的余额为：", money ,"元")
"""
练习
"""
money = 50
fee = 10
fare = 5
print("钱包的余额为：", money ,"元")
print("买冰激凌花费", fee ,"元")
print("买可乐花费", fare ,"元")
money = money - fee - fare
print("最终钱包剩余", money ,"元")