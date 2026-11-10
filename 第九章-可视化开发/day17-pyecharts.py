"""
pyecharts入门
"""
from pyecharts.charts import Line
line = Line() # 创建一个折线图对象
line.add_xaxis(["中国", "美国", "日本"])
line.add_yaxis("GDP", ["10", "20", "30"])
line.render()
