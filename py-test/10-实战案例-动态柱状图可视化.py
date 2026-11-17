"""
GDP柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
# 读取文件
f = open("/Users/wulixiwa/dsh实验室/黑马程序python/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GBK")
data_lines = f.readlines()
print(data_lines)
f.close()
# 将数据转换为字典存储
data_lines.pop(0)
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])      # 年份
    country = line.split(",")[1]        # 国家
    gdp = float(line.split(",")[2])            # gdp
    # 如何判断字典中有没有对应的key呢
    try:
        data_dict[year].append([country, gdp])
    except:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
timeline = Timeline()
# 年份由低到高排序
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element:element[1], reverse=True)
    # 取出本年份gdp前8的国家
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])       # x轴添加国家
        y_data.append(country_gdp[1] / 100000000)       # y轴添加gdp
# 构建柱状图
bar = Bar()
bar.add_xaxis(x_data)
bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
bar.reversal_axis()
timeline.add(bar,str(year))
timeline.add_schema(play_interval=1000,
                    is_timeline_show=True,
                    is_auto_play=True,
                    is_loop_play=False
                    )
timeline.render("/Users/wulixiwa/py-learning/py-test/1960-2019全球GDP数据.html")