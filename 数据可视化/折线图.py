from pyecharts.charts import Line
from pyecharts.globals import CurrentConfig
from pyecharts.options import TitleOpts,LabelOpts,LegendOpts
import json
#CurrentConfig.ONLINE_HOST =""//离线
"""数据处理，x：日期，y：确诊"""
with open("美国.txt",'r',encoding="UTF-8") as f_us:
    us_data=f_us.read()
    us_data=us_data.replace("jsonp_1629344292311_69436(","")
    us_data=us_data[:-2:1]
    us_data = json.loads(us_data)#数据基础处理，，变成合法数据
    us_trend_data=us_data['data'][0]['trend']
    x_us_data=us_trend_data['updateDate'][:314:]#数据轴数据
    y_us_data=us_trend_data['list'][0]['data'][:314:]
with open("日本.txt",'r',encoding="UTF-8") as f_jp:
    jp_data=f_jp.read()
    jp_data=jp_data.replace("jsonp_1629350871167_29498(","")
    jp_data=jp_data[:-2:1]
    jp_data = json.loads(jp_data)#数据基础处理，，变成合法数据
    in_trend_data=jp_data['data'][0]['trend']
    x_jp_data=in_trend_data['updateDate'][:314:]#数据轴数据
    y_jp_data=in_trend_data['list'][0]['data'][:314:]
with open("印度.txt",'r',encoding="UTF-8") as f_in:
    in_data=f_in.read()
    in_data=in_data.replace("jsonp_1629350745930_63180(","")
    in_data=in_data[:-2:1]
    in_data = json.loads(in_data)#数据基础处理，，变成合法数据
    in_trend_data=in_data['data'][0]['trend']
    x_in_data=in_trend_data['updateDate'][:314:]#数据轴数据
    y_in_data=in_trend_data['list'][0]['data'][:314:]
"""全局设置"""
line=Line()
line.add_xaxis(x_us_data)
line.add_yaxis("美国确诊",y_us_data,label_opts=LabelOpts(is_show=False))#label_opts显示图标
line.add_yaxis("日本确诊",y_jp_data,label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊",y_in_data,label_opts=LabelOpts(is_show=False))
line.set_global_opts(
    title_opts=TitleOpts(title="2020美日印三国确诊人数",pos_left="center",pos_top="1%"),
    legend_opts=LegendOpts(pos_bottom="1%")
)
line.render("折线图.html")#括号内为文件名字以及格式，必须在最后，确保设置生效
