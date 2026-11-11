"""
2022年美国新冠确诊人数
"""
import json
from pyecharts.charts import Line
f_us = open("美国.txt", "r", encoding = "UTF-8")
us_data = f_us.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", " ") # 去掉不合理的json头
us_data = us_data[:-2] # 去掉json不合理的尾
us_dict = json.loads(us_data)
us_trend = us_dict["data"][0]["trend"]
us_x_data = us_trend["updataDate"][:314] # x轴数据
us_y_data = us_trend["list"][:314] # y轴数据
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data)
line.render()
f_us.close