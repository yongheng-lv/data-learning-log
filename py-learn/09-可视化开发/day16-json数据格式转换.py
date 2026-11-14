"""
json数据格式转化
"""
import json
list1 = [{"name":"Ete", "gender":"男", "age":19}] # 中文在转换过程中会转换成编码，用ensure_ascii = False 解决
json_str = json.dumps(list1, ensure_ascii = False) # 将列表用json转化成字符串
print(f"经过json格式转化后，数据类型是{type(json_str)}，内容是{json_str}")

dict1 = {"name":"恒", "age":19, "gender":"male"}
json_str1 = json.dumps(dict1, ensure_ascii = False) # 将字典用json转化成字符串
print(f"经过json格式转化后，数据类型是{type(json_str1)}，内容是{json_str1}")

s = '[{"name":"美", "age":19}, {"name":"sun", "age":24}]'
l = json.loads(s) # 将json字符串转换成python数据类型
print(f"经转换后类型是{type(l)},内容是{l}")