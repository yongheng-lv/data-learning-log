# 基本语法：
# 字面量 [元素一，元素二，...]
# 定义变量 变量名称 = [元素一，元素二，...]
# 定义空列表 变量名称 = [] 变量名称 = list()

# name_list = [ "lv", "yong", "heng"]
# print(name_list)
# print(type(name_list))
# 嵌套列表
# my_list = [[ 1, 2, 3],[ 4, 5, 6]]
# print(my_list)
# print(type(my_list))

# 列表的下表索引 从左向右依次从0开始加，从右向左依次从-1开始减
# name_list = [ "lv", "yong", "heng"]
# print(name_list[0])
# 列表的嵌套索引
# name_list = [[ "lv", "yong", "heng"],[ 1, 2, 3]]
# print(name_list[0][1])
# print(name_list[1][-1])

# 列表的常用方法
"""
编号
使用方式
作用
1
列表.append（元素）
向列表中追加一个元素
2
列表.extend（容器）
将数据容器的内容依次取出，追加到列表尾部
3
列表.insert（下标，元素）
在指定下标处，插入指定的元素
4
del列表[下标］
删除列表指定下标元素
5
列表.pop（下标）
删除列表指定下标元素
6
列表.remove（元素）
从前向后，删除此元素第一个匹配项
7
列表.clear（）
清空列表
8
列表.count（元素）
统计此元素在列表中出现的次数
查找指定元素在列表的下标
9
列表.index（元素）
找不到报错ValueError
10
len（列表）
统计容器内有多少元素
"""

# 列表的循环遍历
# index = 0
# mylist = [1, 2, 3, 4, 5]
# while index < len(mylist): # while循环遍历
#     element = mylist[index]
#     print(f"{element}")
#     index += 1

mylist = [1, 2, 3, 4, 5]
for element in mylist:
    print(f"{element}")