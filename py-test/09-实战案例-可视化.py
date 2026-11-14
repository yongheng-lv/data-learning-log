"""
可视化案例
"""
# 折线可视化
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts,LabelOpts
from pyecharts.globals import CurrentConfig
CurrentConfig.ONLINE_HOST = "assets/"   # 用本地资源，不连外网CDN（官网证书过期了）
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
us_y_data = us_trend["list"][0]["data"][:314] # y轴数据，[0]是"确诊"的数字列表
jp_y_data = jp_trend["list"][0]["data"][:314]
in_y_data = in_trend["list"][0]["data"][:314]
line = Line()
line.add_xaxis(us_x_data)
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show = False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show = False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show = False))
line.set_global_opts(title_opts = TitleOpts(title = "2020年美日印新冠感染人数对比折线图", pos_right = "center", pos_bottom = "1%"))
line.render("/Users/wulixiwa/py-learning/py-test/折线图.html")   # 起个名字，免得被下面的地图覆盖
f_us.close()
f_jp.close()
f_in.close()

# 地图可视化
from pyecharts.charts import Map
map = Map()
# add(系列名, 数据, 地图类型)：数据是 (地区名, 数值) 组成的列表
map.add("测试地图", [("California", 100), ("Texas", 50), ("New York", 80)], "美国")
map.render("/Users/wulixiwa/py-learning/py-test/美国地图.html")   # 和折线图分开存



# 导入包
import json
from pyecharts.charts import Map
from pyecharts.options import *
# 读取、关闭文件
f = open("/Users/wulixiwa/dsh实验室/黑马程序python/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
dict_data = json.loads(data) # json转dict
provence_data_list = dict_data["areaTree"][0]["children"]
data_list = []

# 数据里的省名是简称（如"北京"），但地图文件里是全称（如"北京市"）
# 名字对不上，地图就标不上颜色，所以写个小函数转换一下
def change_name(name):
    if name in ["北京", "上海", "天津", "重庆"]:
        return name + "市"                    # 四个直辖市
    if name == "内蒙古":
        return "内蒙古自治区"
    if name == "广西":
        return "广西壮族自治区"
    if name == "西藏":
        return "西藏自治区"
    if name == "宁夏":
        return "宁夏回族自治区"
    if name == "新疆":
        return "新疆维吾尔自治区"
    if name == "台湾":
        return "台湾省"
    if name in ["香港", "澳门"]:
        return name + "特别行政区"
    return name + "省"                        # 剩下的都是省

for provence_data in provence_data_list:
    provence_name = change_name(provence_data["name"])   # 简称转全称
    provence_confirm = provence_data["total"]["confirm"]
    data_list.append((provence_name, provence_confirm))
print(data_list)
map = Map()
map.add("各省确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1, "max":99, "label":"1~99人", "color":"#CCFFFF"},
            {"min":100, "max":999, "label":"100~999人", "color":"#FFFF99"},
            {"min":1000,"max": 4999,"label":"1000~4999人","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000~9999人","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000~99999人","color":"#CC3333"},
            {"min":100000,"label":"100000+","color":"#990033"},
        ]
    )
)
map.render("/Users/wulixiwa/py-learning/py-test/全国疫情地图.html")