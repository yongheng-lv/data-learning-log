"""
文件
"""
# 编码：一种集合规则，记录了内容和二进制间相互转化的逻辑，编码有许多，最常用的是UFT-8；编码能将各种语言翻译成0和1，让计算机读取并保存；反之，让计算机把0和1翻译成各种语言也可以
f = open("/Users/wulixiwa/Documents/test.txt", "r", encoding="UTF-8") # 打开文件
print(f"打开的测试文件是{f}，类型是{type(f)}")

context = f.read() # 读取文件，四个字节
context2 = f.read(4) # 读取余下全部字节
print(f"读取四个字节的文件内容是{context}，读取的全部内容是{context2}") # 从第一次读取的文件内容后继续读取
lines = f.readlines() # 括号内不填，默认读取余下的全部行，封装在列表中
print(f"余下的内容是{lines}，类型是{type(lines)}")
line1 = f.readline() # 读取余下的第一行数据
line2 = f.readline()
line3 = f.readline()
print(f"{line1}{line2}{line3}")
for line in f:
    print(f"每一行数是{line}") # 读取余下的行，输出字符串

import time
f.close() # 关闭文件，不关闭无法在访达对原文件进行修改
time.sleep(5000) # 睡眠5000秒，不等同关闭
with open("/Users/wulixiwa/Documents/test.txt", "r", encoding = "UTF-8") as f: # with open语法运行完后自动关闭
    for i in f:
        print(f"每一行内容是{i}")

f = open("/Users/wulixiwa/Documents/write.txt", "w", encoding = "UTF-8")
f.write("hello world") # 若文件存在则覆盖原文件内容，不存在则添加文件
# f.flush() # 刷新后内容会更新
f.close() # 关闭文件，内置刷新功能
print("成功")

f = open("/Users/wulixiwa/Documents/write.txt", "a", encoding = "UTF-8")
f.write("\n") # 换行
f.write("你好，世界") # 在write文件后追加“你好世界”
f.close()