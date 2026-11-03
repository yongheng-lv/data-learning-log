"""
集合
"""
set1 = set() # 空集
set2 = {1, 2, 3, 4, 5, 2}
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
# 将集合清空
set2.clear()
print(f"清空后，set2为{set2}")
