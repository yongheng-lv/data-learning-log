import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# 设置画布大小
plt.figure(figsize=(8, 6))

# 数据输入
# 参数顺序：A, B, C, AB, AC, BC, ABC
# 因为我们只知道这几个，其他的填 0 或推算的值
# 为了强行画出图，这里输入的是逻辑面积
venn3(subsets=(1, 1, 1, 0, 1, 1, 0), 
      set_labels=('A', 'B', 'C'))

plt.title("Venn Diagram (Logic Only)")
plt.show()