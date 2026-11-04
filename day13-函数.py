"""
函数
"""
def test_return():
    return 1, 2, "hell0"
x, y, z= test_return() # 函数的多返回值
print(f"函数test_return的返回值为{x}和{y}和{z}")

def user_info(name,age,addr):
    print(f"姓名是{name}, 年龄是{age}, 住在{addr}")
user_info("恒", "19", "北京") # 位置传参
def user_info2(name,age,gender):
    print(f"姓名是{name}, 年龄是{age}, 性别是{gender}")
user_info2(name = "恒", gender = "男", age = 19) # 关键字传参，可调换位置
def user_info3(name,age = 19,gender = "男"): # 默认参数，gender = "男"为默认参数，若不传参，则使用默认参数，且默认参数必须放在非默认参数的后面
    print(f"姓名是{name}, 年龄是{age}, 性别是{gender}")
user_info3("恒", 20) # 位置传参，使用默认参数
user_info3("恒", 20, "女") # 位置传参，使用传入的参数
user_info3("恒", gender = "女") # 关键字传参，使用传入的参数