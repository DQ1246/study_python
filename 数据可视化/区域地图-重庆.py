from pyecharts.charts import Map
from pyecharts.options import LabelOpts,VisualMapOpts
import json
map=Map()
with open("疫情.txt",'r',encoding="UTF-8") as f1:#自动关闭文件
    d=json.loads(f1.read())
    data_name=d["areaTree"][0]["children"][18]["children"]#获取区县与人数的最大层级
    data = []
    for x in range(0,40):#获取区县与人数具体路径
        data.append((data_name[x]["name"],data_name[x]["total"]["confirm"]))
    map.add("重庆疫情图",data,"重庆",label_opts=LabelOpts(is_show=False))#隐藏图标
    map.set_global_opts(#全局设置
        visualmap_opts=VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=[{"min": 0,"max":0,"label": "0人", "color": "#ffffff"},
                    {"min": 1, "max": 9, "label": "1~9人", "color": "#B0E2FF"},
                    {"min": 10, "max": 49, "label": "10~49人", "color": "#00FF00"},
                    {"min": 50, "max": 99, "label": "50~99人", "color": "#20B2AA"},
                    {"min": 100, "label": "100以上", "color": "#FFA500"}
                    ]
        )
    )
    map.render("重庆疫情图.html")