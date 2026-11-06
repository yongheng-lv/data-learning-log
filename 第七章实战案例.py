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
list1 = f.readlines()
for i in list1:
    num = 0
    if i == "itheima":
        num += 1
        print(f"itheima 共有{num}个")