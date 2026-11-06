"""
文件
"""
# 编码：一种集合规则，记录了内容和二进制间相互转化的逻辑，编码有许多，最常用的是UFT-8；编码能将各种语言翻译成0和1，让计算机读取并保存；反之，让计算机把0和1翻译成各种语言也可以
f = open("/Users/wulixiwa/Documents/test.txt", "r", encoding="UTF-8") # 打开文件
print(f"打开的测试文件是{f}，类型是{type(f)}")
context = f.read(4) # 读取文件
print(f"读取的文件内容是{context}")
line = f.readline() # 括号内不填，默认一行
print(f"{line}")