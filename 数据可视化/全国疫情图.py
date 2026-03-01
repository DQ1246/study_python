from pyecharts.charts import Map
from pyecharts.options import LabelOpts,VisualMapOpts
import json
map=Map()
with open("疫情.txt",'r',encoding="UTF-8") as f1:#自动关闭文件
    d=json.loads(f1.read())
    data_name=d["areaTree"][0]["children"]#获取省份与人数的最大层级
    data = []
    for x in range(0,34):#获取省份与人数具体路径
        data.append((data_name[x]["name"],data_name[x]["total"]["confirm"]))
    map.add("全国疫情图",data,"china",label_opts=LabelOpts(is_show=False))#隐藏图标
    map.set_global_opts(#全局设置
        visualmap_opts=VisualMapOpts(
            is_show=True,
            is_piecewise=True,
            pieces=[{"min": 0,"max":0,"label": "0人", "color": "#ffffff"},
                    {"min": 1, "max": 99, "label": "1~99人", "color": "#B0E2FF"},
                    {"min": 100, "max": 499, "label": "100~499人", "color": "#00FF00"},
                    {"min": 500, "max": 999, "label": "500~999人", "color": "#20B2AA"},
                    {"min": 1000, "max": 4999, "label": "1000~4999", "color": "#FFA500"},
                    {"min": 5000, "max": 9999,"label": "5000~9999", "color": "#FF7F50"},
                    {"min": 10000, "max": 19999,"label": "10000~19999", "color": "#FF6347"},
                    {"min": 20000, "max": 49999,"label": "20000~49999", "color": "#FF0000"},
                    {"min": 50000,"label": "50000以上", "color": "#A52A2A"},]
        )
    )
    map.render("全国疫情图.html")