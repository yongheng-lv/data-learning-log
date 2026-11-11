"""
2022年美国新冠确诊人数
"""
import json
from pyecharts.charts import Line
f_us = open("/Users/wulixiwa/dsh实验室/黑马程序python/美国.txt", "r", encoding = "UTF-8")
f_jp = open("/Users/wulixiwa/dsh实验室/黑马程序python/日本.txt", "r", encoding = "UTF-8")
f_in= open("/Users/wulixiwa/dsh实验室/黑马程序python/印度.txt", "r", encoding = "UTF-8")
us_data = f_us.read()
jp_data = f_jp.read()
in_data = f_in.read()
us_data = us_data.replace("jsonp_1629344292311_69436(", " ") # 去掉不合理的json头
jp_data = jp_data.replace("jsonp_1629350871167_29498(", " ") 
in_data = in_data.replace("jsonp_1629350745930_63180(", " ")
us_data = us_data[:-2] # 去掉json不合理的尾
jp_data = jp_data[:-2]
in_data = in_data[:-2]
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)
us_trend = us_dict["data"][0]["trend"]
jp_trend = jp_dict["data"][0]["trend"]
in_trend = in_dict["data"][0]["trend"]
us_x_data = us_trend["updateDate"][:314] # x轴数据
us_y_data = us_trend["list"][:314] # y轴数据
jp_y_data = jp_trend["list"][:314]
in_y_data = in_trend["list"][:314]
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data)
line.add_yaxis("日本确诊人数", jp_y_data)
line.add_yaxis("印度确诊人数", in_y_data)
line.render()
f_us.close