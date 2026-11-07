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