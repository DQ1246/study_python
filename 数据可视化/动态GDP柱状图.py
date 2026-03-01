from pyecharts.charts import Bar,Timeline
from pyecharts.options import LabelOpts,TitleOpts,LegendOpts
from pyecharts.globals import ThemeType
"""x1:初始每行数据，包含年、GDP、国家
   x2:年，用于创建以年为排序的列表，包含GDP、国家
   x3:年，用于排序的定位，提取GDP前八的数据信息
   x4:年，用于排序的定位，将GDP、国家的数据分开"""
timeline=Timeline(
    {"theme": ThemeType.LIGHT}#主题
)
"""数据处理"""
with open("1960-2019全球GDP数据.csv", 'r', encoding="GB2312") as f:#提数据
    data_line=f.readlines()
data_line.pop(0)#除去标头
data_dict={}#把数据转化为字典，为了x、y轴
for x1 in data_line:
    a=x1.split(",")
    year=int(a[0])
    country=a[1]
    GDP=float(a[2])
    try:#判断错误，防止没有对象
        data_dict[year].append([country,GDP])
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append([country, GDP])
"""年排序"""
year_list=[]
for x2 in data_dict:
    year_list.append(x2)#可用字典的keys
year_list=sorted(year_list)
for x3 in year_list:
    data_dict[x3].sort(key=lambda element:element[1],reverse=True)#GDP降序
    year_data=data_dict[x3][0:8]#GDP前8的国家
    x_axis=[]#x轴数据
    y_axis=[]#y轴数据
    for x4 in year_data:
        y_axis.append(x4[1]/100000000)
        x_axis.append(x4[0])
    bar=Bar()
    bar.add_yaxis("GDP(亿)",y_axis,label_opts=LabelOpts(position="right"))
    bar.add_xaxis(x_axis)
    x_axis.reverse()
    y_axis.reverse()
    bar.reversal_axis()#反转x、y轴
    bar.set_global_opts(#全局设置
        title_opts=TitleOpts(title=f"{x3}年GDP全球前八国家排名",pos_top="1%",pos_right="center"),
        legend_opts=LegendOpts(pos_bottom="1%")
    )
    timeline.add(bar,x3)
timeline.add_schema(
    play_interval=800,#时间间隔，单位毫秒
    is_timeline_show=False,#展示时间线
    is_auto_play=True,#自动播放
    is_loop_play=True#循环播放
)
timeline.render("1960~2019全球GDP前8国家排名.html")