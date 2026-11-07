"""
异常
"""
try: # 内含可能异常的语句
    f = open("/Users/wulixiwa/Documents/123.txt", "r", encoding = "UTF-8")
except Exception as e: # 捕获所有类型异常，并执行其包含的语句
    print(f"捕获到异常了，是{e}")

try:
    num = 1 / 0
except ZeroDivisionError as e: # 捕获指定类型的异常 
    print(f"太好了，捕获到异常了,是{e}类型的")

    try:
        num = 1 / 0
        print(name)
    except (NameError,ZeroDivisionError): # 捕获指定的多个异常
        print("太好了，成功捕获到了异常")

def func1():
    print(name)
def func2():
    func1()
    print("yes")
def main(): # 异常具有传递性
    try:
        func2()
    except Exception as e:
        print(f"异常传递下来了，类型是{e}")
main()

import time # 倒入time模块，能够使用其内部的功能
print("hello")
time.sleep(5) # 使用time模块内部的sleep方法，睡眠5秒
print("nihao")

from time import sleep # 导入指定模块
print("ni")
sleep(2)
print("hao")

from time import *
print(3)
sleep(5)
print(4)