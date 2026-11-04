"""
有一个列表，内容是：［21,25,21,23,22,20］，记录的是一批学生的年龄
请通过列表的功能（方法），对其进行
1
定义这个列表，并用变量接收它
2
追加一个数字31，到列表的尾部
3
追加一个新列表［29，33，30］，到列表的尾部
4
取出第一个元素（应是：21）
5
取出最后一个元素（应是：30）
6
查找元素31，在列表中的下标位置
"""
# stu_age = [ 21, 25, 21, 23, 22, 20]
# stu_age.append(31)
# new_list = [ 29, 33, 30]
# stu_age.extend(new_list)
# num1 = stu_age[0]
# num2 = stu_age[-1]
# num3 = stu_age.index(31)
# print(f"{stu_age}\n{num1}\n{num2}\n{num3}")

"""
定义一个列表，内容是：［1, 2, 3, 4, 5, 6, 7, 8, 9, 10］
• 遍历列表，取出列表内的偶数，并存入一个新的列表对象中
• 使用while循环和for循环各操作一次
通过while循环，从列表：［1，2，3，4，5，6，7，8，9，10］中取出偶数，组成新列表：［2，4，6，8，10］
通过for循环，从列表：[1，2，3，4，5，6，7，8，9，10］中取出偶数，组成新列表：【2，4,6，8,10］
提示：
• 通过if判断来确认偶数
• 通过列表的append方法，来增加元素
"""
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = []
# index = 1
# while index <= len(list1):
#     if index % 2 == 0:
#         list2.append(index)
#     index += 1
# print(f"{list2}")
# list1 = [1, 2, 3, 4 ,5 ,6 ,7 ,8, 9, 10]
# list2 = []
# for element in list1:
#     if element % 2 == 0:
#         list2.append(element)
# print(f"{list2}")
"""
定义一个元组，内容是：
（'周杰轮，11，［ football，'music'］），记录的是一个学生的信息（姓名、年
龄、爱好）
请通过元组的功能（方法），对其进行
1． 查询其年龄所在的下标位置
2. 查询学生的姓名
3. 删除学生爱好中的football
4．增加爱好：coding到爱好list内
"""
# t1 = ('周杰伦', 11, [ 'football', 'music'])
# index = t1.index(11)
# name = t1[0]
# del t1[2][1]
# # t1[2].append("coding")
# t1[2].insert(0,"coding")
# print(f"{index}{name}{t1}")

"""
给定一个字符串："itheima itcast boxuegu'
•统计字符串内有多少个"it"字符
• 将字符串内的空格，全部替换为字符：|
• 并按照”进行字符串分割，得到列表
字符串itheima itcast boxvegu中有：2个it字符
字符串itheima itcast boxuegu，被替换空格后，结果：itheimalitcast|boxuegu
字符串itheimalitcast|boxuegu，按照|分隔后，得到：［'itheima'，'itcast'，'boxvegu'］
"""
# str = "itheima itcast buxuegu"
# num = str.count("it")
# new_str = str.replace(" ","|")
# new_str_list = new_str.split("|")
# print(f"{num}\n{new_str}\n{new_str_list}")

"""
有字符串："万过薪月，灵序穆马黑来，nohtyP学"
• 请使用学过的任何方式，得到"黑马程序员"
"""
# my_str = "万过薪月，员序程马黑来，nohtyP学"
# my_str2 = my_str[::-1][9:14:1]
# print(f"result = {my_str2}")

"""
有如下列表对象：
my_list=［'黑马程序员'，传智播客，'黑马程序员'，'传智播客'，'itheima'， "itcast， 'itheima'， "itcast，
'best'］
请：
• 定义一个空集合
• 通过for循环遍历列表
• 在for循环中将列表的元素添加至集合
• 最终得到元素去重后的集合对象，并打印输出
"""
set1 = set()
my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima', 'itcast', 'itheima', 'itcast','best']
for element in my_list:
    set1.add(element)
print(set1)