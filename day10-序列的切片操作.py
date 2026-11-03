"""
序列（列表、元组、字符串）的切片操作
"""
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_str = "itheima itcast boxuegu"
mt_tuple = ('周杰伦', 11, ['football', 'music'])
# 列表切片
# 列表[起始下标:结束下标:步长]
new_list = my_list[0:10:2]
print(f"列表切片结果是{new_list}")
# 字符串切片
# 字符串[起始下标:结束下标:步长]
new_str = my_str[0:20:2]
print(f"字符串切片结果是{new_str}")
# 元组切片
# 元组[起始下标:结束下标:步长]
new_tuple = mt_tuple[0:2:1]
print(f"元组切片结果是{new_tuple}")

new_str2 = "万过薪月，员序程马黑来,nohtyP学"
new_str3 = new_str2[9:4:-1]
print(f"新字符串切片结果是 {new_str3}")