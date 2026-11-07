from my_model import * # 导入全部功能 
test_a(2, 3)
# test_b(3, 2) # my_model 模块中__all__不包含test_b，因此无法调用
import my_model
my_model.test_a(3, 4) 
