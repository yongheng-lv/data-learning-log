"""
数据类型+数据类型转换+标识符
"""
# 数据类型

# 使用print语句直接输出数据类型
print(type(666))
print(type(13.14))
print(type("黑马程序员"))
# 使用变量存储type（）语句的结果(type语句可以返回结果，学到的第一个可以返回结果的语句，print语句只能打印结果，不能返回结果)
int_type = type(666)
float_type= type(13.14)
string_type = type("黑马程序员")
print(int_type)
print(float_type)
print(string_type)
# 使用type语句查看变量中存储的数据类型
name = "黑马程序员"
name_type = type(name)
print(name_type)
# 数据类型的转换

# 将数字类型转换成字符串
num_str = str(11)
print(type(num_str), num_str)
num_str2 = str(13.14)
print(type(num_str2))
# 将字符串转换成数字类型
int("11")
num_int = int("11")
print(type(num_int))
float("13.14")
num_float = float("13.14")
print(type(num_float))
# 错误示范，将含有文字的字符串转换成数字类型（会报错），万物皆可转字符串，字符串仅仅能转换成数字类型的前提是字符串中仅仅包含数字
# num_int = int("黑马程序员")
# print(type(num_int))

# 标识符

# 规则1：内容限定为字母、数字、下划线，且不能以数字开头
# 错误示范
# 1name = "黑马程序员"
# _name = "黑马程序员"
# 规则2：不能使用python中的关键字作为标识符
# 错误示范
# if = "黑马程序员"
# 规则3：大小写敏感
# Aplle = "苹果"
# apple = "香蕉"