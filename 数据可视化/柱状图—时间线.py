from pyecharts.charts import Bar,Timeline
from pyecharts.globals import ThemeType
bar1=Bar()
bar1.add_xaxis(["红","蓝","绿"])
bar1.add_yaxis("level",[1,2,3])
bar2=Bar()
bar2.add_xaxis(["红","蓝","绿"])
bar2.add_yaxis("level",[3,6,1])
bar3=Bar()
bar3.add_xaxis(["红","蓝","绿"])
bar3.add_yaxis("level",[4,10,5])
timeline=Timeline(
    {"theme":ThemeType.LIGHT}#主题
)
timeline.add(bar1,"A")
timeline.add(bar2,"B")
timeline.add(bar3,"C")
"""自动播放"""
timeline.add_schema(
    play_interval=1000,#时间间隔，单位毫秒
    is_timeline_show=False,#展示时间线
    is_auto_play=True,#自动播放
    is_loop_play=False#循环播放
)
timeline.render("柱状图-时间线.html")