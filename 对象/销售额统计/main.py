from data import record
from file import filereader,textfilereader,jsonfilereader
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType
text_record=textfilereader("2011年1月销售数据.txt")
json_record=jsonfilereader("2011年2月销售数据JSON.txt")
text_data=text_record.reader()
json_data=json_record.reader()
all_data=text_data+json_data#所有数据
data_dict={}
for x in all_data:#字典，统计当天的销售额
    if x.date in data_dict.keys():#同天有多种销售额
        data_dict[x.date]+=x.money
    else:
        data_dict[x.date]=0

bar=Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额",list(data_dict.values()),label_opts=LabelOpts(is_show=False))
bar.set_global_opts(#全局设置
        title_opts=TitleOpts(title="销售额",pos_top="1%",pos_right="center"),
        legend_opts=LegendOpts(pos_bottom="1%")
    )
bar.render("销售额统计.html")
#离线文件在“数据可视化/echarts.min.js”