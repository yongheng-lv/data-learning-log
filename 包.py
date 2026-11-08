"""
测试自定义包
"""
import my_package.my_model1
my_package.my_model1.func1()

from my_package import my_model2
my_model2.func2()

from my_package.my_model2 import func2
from my_package.my_model1 import func1
func1()
func2()

from my_package import * # 只导入all函数里的功能
my_model1.func1()