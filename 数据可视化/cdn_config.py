CDN_URLS = {
    "jsdelivr": "https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/",#jsdelivr和bootcdn国内快一点
    "unpkg": "https://unpkg.com/echarts@5.4.3/dist/",
    "bootcdn": "https://cdn.bootcdn.net/ajax/libs/echarts/5.4.3/"
}
# 默认使用哪个 CDN（可修改）
DEFAULT_CDN = "jsdelivr"
# 使用方法
#import cdn_config
#from pyecharts.globals import CurrentConfig//调用CurrentConfig.ONLINE_HOST
#selected_cdn = cdn_config.CDN_URLS[cdn_config.DEFAULT_CDN]
#CurrentConfig.ONLINE_HOST = selected_cdn