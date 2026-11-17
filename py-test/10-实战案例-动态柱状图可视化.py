"""
GDP柱状图开发
"""
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
sorted_year_list = sorted(data_dict.keys())
print(sorted_year_list)