"""
异常
"""
try:
    f = open("/Users/wulixiwa/Documents/123.txt", "r", encoding = "UTF-8")
except Exception as e:
    print(f"捕获到异常了，是{e}")