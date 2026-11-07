"""
自定义模块
"""
__all__ = ['test_a']
def test_a(a, b):
    print(a + b)
if __name__ == "__main__": # 不会调用以下函数
    test_a(1, 2)

def test_b(a, b):
    print(a - b)