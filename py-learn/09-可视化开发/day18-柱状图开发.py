# 基础柱状图
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar = Bar()
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position = "right"))
bar.reversal_axis()
bar.render("/Users/wulixiwa/py-learning/py-learn/基础柱状图.html")

# 基础时间线柱状图
from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position = "right"))
bar1.reversal_axis()
bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [40, 25, 15], label_opts=LabelOpts(position = "right"))
bar2.reversal_axis()
bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [50, 30, 20], label_opts=LabelOpts(position = "right"))
bar3.reversal_axis()
# 构建时间线
timeline = Timeline()
timeline.add(bar1, "1")
timeline.add(bar2, "2")
timeline.add(bar3, "3")
timeline.render("/Users/wulixiwa/py-learning/pt-learn/基础时间柱状图.html")