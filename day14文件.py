"""
文件
"""
# 编码：一种集合规则，记录了内容和二进制间相互转化的逻辑，编码有许多，最常用的是UFT-8；编码能将各种语言翻译成0和1，让计算机读取并保存；反之，让计算机把0和1翻译成各种语言也可以
f = open("/Users/wulixiwa/Documents/test.txt", "r", encoding="UTF-8") # 打开文件
print(f"打开的测试文件是{f}，类型是{type(f)}")

# context = f.read() # 读取文件，四个字节
# context2 = f.read(4) # 读取余下全部字节
# print(f"读取四个字节的文件内容是{context}，读取的全部内容是{context2}") # 从第一次读取的文件内容后继续读取
# lines = f.readlines() # 括号内不填，默认读取余下的全部行，封装在列表中
# print(f"余下的内容是{lines}，类型是{type(lines)}")
# line1 = f.readline() # 读取余下的第一行数据
# line2 = f.readline()
# line3 = f.readline()
# print(f"{line1}{line2}{line3}")

for line in f:
    print(f"每一行数是{line}")