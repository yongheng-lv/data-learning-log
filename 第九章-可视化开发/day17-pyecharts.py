"""
pyecharts入门
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, VisualMapOpts, ToolboxOpts
line = Line() # 创建一个折线图对象
line.add_xaxis(["中国", "美国", "日本"])
line.add_yaxis("GDP", ["10", "20", "30"])
line.set_global_opts( # 配置全局设置set_global_ops设置
    title_opts=TitleOpts(title = "GDP展示", pos_left="centre", pos_bottom="1%"),
    toolbox_opts=ToolboxOpts(is_show=True),
    legend_opts=LegendOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
)
line.render()
