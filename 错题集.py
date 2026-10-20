"""
通过for循环，输出如下九九乘法表内容
"""
for i in range(1,10):
    for j in range(1,i + 1): 
        print(f"{i} * {j} = {i * j}\t",end='')
    print()