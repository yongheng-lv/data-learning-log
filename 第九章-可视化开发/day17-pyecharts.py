"""
pyecharts入门
"""
# 折线图可视化
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts, ToolboxOpts
line = Line() # 创建一个折线图对象
line.add_xaxis(["中国", "美国", "日本"])
line.add_yaxis("GDP", ["10", "20", "30"])
line.set_global_opts( # 配置全局设置set_global_ops设置
    title_opts=TitleOpts(title = "GDP展示", pos_left="center"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()

# 地图可视化
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [
    ("北京", 9),
    ("山东", 99),
    ("广东", 199),
    ("新疆", 299),
    ("青海", 399),
    ("台湾", 499)
]
map.add("测试地图",data, "China") # 添加数据
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
    is_show=True,
    is_piecewise=True,
    pieces=[
        {"min":1, "max":9, "label":"1-99", "color":"#CCFFFF"}, 
        {"min":100, "max":300, "label":"100-300","color":"#FF6666"}, 
        {"min":301, "max":500, "label":"301-500", "color":"#990033"}
        ]
    )
)
map.render()