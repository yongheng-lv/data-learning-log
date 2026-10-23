"""
定义一个函数，函数名任意，要求调用函数后可以输出如下欢迎语：
欢迎来到黑马程序员！
请出示您的健康码以及72小时核酸证明！
"""
# def 欢迎():
#     print("欢迎来到黑马程序员！\n请出示您的健康码以及72小时核酸证明！")
# 欢迎()

"""
定义一个函数，名称任意，并接受一个参数传入（数字类型，表示体温）
在函数内进行体温判断（正常范围：小于等于37.5度），并输出如下内容：
欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！
体温测量中，您的体温是：37.3度，体温正常请进！
欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！
体温测量中，您的体温是：39.3度，需要隔离！
"""
# def wendu(x):
#     if x <= 37.5:
#         print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！\n体温测量中，您的体温是{x}度，体温正常请进！")
#     else:
#         print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并哦诶和测量体温！\n体温测量中，您的体温是{x}度，需要隔离！")
# wendu(39.9)

"""
• 定义一个全局变量：money，用来记录银行卡余额（默认5000000）
• 定义一个全局变量：name，用来记录客户姓名（启动程序时输入）
• 定义如下的函数：
• 查询余额函数
• 存款函数
• 取款函数
• 主菜单函数
• 要求：
• 程序启动后要求输入客户姓名
• 查询余额、存款、取款后都会返回主菜单
• 存款、取款后，都应显示一下当前余额
• 客户选择退出或输入错误，程序会退出，否则一直运行
"""
# 定义全局变量money name
money = 5000000
# 要求客户输入姓名
name = input("请输入姓名：")
# 定义查询函数
def check_balance(show_tatol):
    if show_tatol:
        print("----------查询余额----------")
    print(f"{name}，您好，您的余额是{money}元")
# 定义存款函数
def saving(num):
    global money # money在函数内定义为全局变量
    money += num
    print("-----------存款-----------")
    print(f"{name}，您好，您存款{num}元成功")
# 调用check_balance函数查询余额
    check_balance






















# money = 5000000
# name = input("请输入姓名：")
# def check_balance():
#     print(f"{name},您好，您的余额为{money}元")
# def cash_deposit():
#     cash1 = int(input("请输入存款金额："))
#     print(f"{name}您好，存款{cash1}成功\n当前账户余额为{money + cash1}")
# def cash_withdraw():
#     cash2 = int(input("请输入取款金额："))
#     print(f"{name}您好，取款{cash2}成功\n当前账户余额为{money - cash2}")
# def main_menu():
#     print(f"{name},您好，欢迎来到永亨银行ATM，请选择操作：\n查询余额【输入1】\n存款【输入2】\n取款【输入3】\n退出【输入4】")
#     sel = int(input("请输入您的选择："))
#     while sel == 1:
#         check_balance()
#         main_menu()
#     while sel == 2:
#         cash_deposit()
#         main_menu()
#     while sel == 3:
#         cash_withdraw()
#         main_menu()
#     while sel >= 4 :
#         break
# main_menu()
# 缺点：
# 函数要改全局变量，必须 global
# 重复做同一件事用循环，不要用递归
# 一次判断用 if，反复执行才用 while


