"""
itheima itcast python
itheima python itcast
bejing shanghaiitheima
shenzhen guangzhou itheima
wuhan hangzhou itheima
zhengzhou bigdata itheima
通过文件读取操作，读取此文件，统计itheima单词出现的次数
"""
f = open("/Users/wulixiwa/Documents/test.txt", "r", encoding = "UTF-8")
num = 0
for list1 in f: # 输出字符串
    list1 = list1.strip()
    words = list1.split(" ")
    for word in words:
        if word == "itheima":
            num += 1
print(f"itheima 共有{num}个")

"""
读取文件
将文件写出到bill.txt.bak文件作为备份
同时，将文件内标记为测试的数据行丢弃
"""
f = open("/Users/wulixiwa/Documents/bill.txt", "r", encoding = "UTF-8")
info = f.read()
print(info)