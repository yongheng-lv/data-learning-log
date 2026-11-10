"""
pyecharts入门
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts
line = Line() # 创建一个折线图对象
line.add_xaxis(["中国", "美国", "日本"])
line.add_yaxis("GDP", ["10", "20", "30"])
line.set_global_opts(
    title_opts=TitleOpts(title = "GDP展示")
)
line.render()
