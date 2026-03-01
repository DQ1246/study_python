from pyecharts.charts import Map
from pyecharts.globals import CurrentConfig
from pyecharts.options import VisualMapOpts,LabelOpts
#CurrentConfig.ONLINE_HOST="https://lib.baomitu.com/echarts/5.4.3/"//离线or在线（没有包）
map=Map()
data=[
    ("北京市",100),
    ("重庆市",200),
    ("天津市",300),
    ("上海市",400)
]
map.add("中国地图",data,"china",label_opts=LabelOpts(is_show=False))
"""全局设置"""
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[{"min":1,"max":99,"label":"1~99人","color":"#E0FFFF"},
               {"min":100,"max":199,"label":"100~199人","color":"#00FFFF"},
               {"min":200,"max":299,"label":"200~299人","color":"#FF7F50"},
               {"min":300,"max":399,"label":"300~399人","color":"#FF0000"},
               {"min":400,"max":499,"label":"400~499","color":"#8B0000"},
               {"min":500,"label":"500以上","color":"#8B0000"}]
    )
)
map.render("基础地图.html")