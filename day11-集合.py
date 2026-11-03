"""
集合
"""
set1 = set() # 空集
set2 = {1, 2, 3, 4, 5, 2}
set3 = {1, 7, 8}
print(f"set2的值是: {set2},类型是：{type(set2)}") # 自动去重
# 集合内添加一个元素
set2.add(6)
print(f"添加新元素后set2为: {set2}")
# 移除集合内指定的元素
set2.remove(1)
print(f"移除指定元素后set2为:{set2}")
# 从集合中随机取出一个元素
num = set2.pop()
print(f"在set里随机取出的数为{num}")
# 得到一个新集合，内含2个集合的差集原有的2个集合内容不变
set4 = set2.difference(set3)
print(f"set2和set3的差集为{set4}")
# 在集合2中，删除集合3中存在的元素集合2被修改，集合3不变
set2.difference_update(set3)
print(f"在set2中删除set3中的元素后，set2为{set2}")
# 得到1个新集合，内含2个集合的全部元素,原有的2个集合内容不变
set5 = set2.union(set3)
print(f"set2和set3的并集为{set5}")
# 导到一个整数，记录了集合的元素数量
new_num = len(set2)
print(f"set2的元素数量为{new_num}")
# 将集合清空
set2.clear()
print(f"清空后，set2为{set2}")
