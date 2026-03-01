from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
bar=Bar()
bar.add_xaxis(["红","蓝","绿"])
bar.add_yaxis("level",[1,2,3],label_opts=LabelOpts(position="right"))#数值标签位置
bar.reversal_axis()
bar.render("柱状图反转.html")