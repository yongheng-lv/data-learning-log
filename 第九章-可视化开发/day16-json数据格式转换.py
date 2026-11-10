"""
json数据格式转化
"""
import json
data = [{"name":"Ete", "gender":"male", "age":19}]
json_str = json.dumps(data)
print(f"经过json格式转化后，数据类型是{type(json_str)}，内容是{json_str}")