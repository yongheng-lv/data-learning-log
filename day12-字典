"""
字典
"""
# my_dict = {}  / my_dict = dict() # 定义空字典
my_dict1 = {"name":"lv yong heng" , "age":19, "learning":"python"} # 定义字典
print(f"输出字典my_dict的值为{my_dict1},类型是{type(my_dict1)}")
my_dict1["name"]
print(f"通过字典查找键name所对应的值为{my_dict1["name"]}") # 查找键所对应的值
my_dict2 = {"lvyongheng":{"gender":"male", 
                          "age":19}, 
            "james":{"gender":"male", 
                     "age":40}, 
             "jack":{"gender":"male", 
                     "age":25}, 
            "lili":{"gender":"female", 
                    "age":24}
            }# 字典嵌套
my_dict2["lvyongheng"]["age"] # 查找嵌套字典中键所对应的值
print(f"通过嵌套字典查找键lvyongheng所对应的age值为{my_dict2['lvyongheng']['age']}" )
my_dict2 = {"周杰轮":99, "林俊节":88, "张学油":77}
score = my_dict2["张学油"] # 查找键所对应的值
print(f"通过字典查找键张学油所对应的值为{score}")
my_dict2["张信哲"] = 66 # 添加键值对
my_dict2["周杰伦轮"] = 33 # 修改键值对
print(f"添加和修改键值对后，my_dict2的值为{my_dict2}")
score2 = my_dict2.pop("林俊节") # 删除键值对
print(f"删除的键值对为{score2},删除后my_dict2的值为{my_dict2}")
# my_dict2.clear() # 清空字典
# print(f"清空后my_dict2的值为{my_dict2}")
len(my_dict2) # 得到字典的长度
print(f"字典的长度为{len(my_dict2)}")
# ⚠️以下为遗忘
keys = my_dict2.keys() # 通过keys()方法获取字典的所有键
for key in keys:
    print(f"字典里所有的键有{keys}")
    print(f"字典中{key}的值是{my_dict2[key]}")
