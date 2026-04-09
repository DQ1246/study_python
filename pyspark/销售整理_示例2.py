from pyspark import SparkConf,SparkContext
import os,json
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
conf=SparkConf().setMaster("local[*]").\
    setAppName("test")
sc=SparkContext(conf=conf)
rdd=sc.textFile("orders.txt")
rdd1=rdd.flatMap(lambda x:x.split("|"))#json数据分割
rdd2=rdd1.map(lambda x:json.loads(x))#json转化dict
#城市销售额排名
rdd3=rdd2.map(lambda x:(x["areaName"],int(x["money"])))#二元元组
rdd4=rdd3.reduceByKey(lambda x,y:x+y)
rdd5=rdd4.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print("城市销售额排名：")
for x in rdd5.collect():
    print(f"城市：{x[0]},金额：{x[1]}")
#商品品类
rdd6=rdd2.map(lambda x:x["category"])
rdd7=rdd6.distinct()#去重
print(f"商品品类：{rdd7.collect()}")
#北京市的商品品类
rdd8=rdd2.filter(lambda x:x["areaName"]=="北京")#北京数据
rdd9=rdd8.map(lambda x:x["category"]).distinct()
print(f"北京市的商品品类：{rdd9.collect()}")