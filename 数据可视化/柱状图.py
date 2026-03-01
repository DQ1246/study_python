from pyecharts.charts import Bar
bar=Bar()
bar.add_xaxis(["红","蓝","绿"])
bar.add_yaxis("level",[1,2,3])
bar.render("柱状图.html")