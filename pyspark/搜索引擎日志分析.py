from pyspark import SparkConf,SparkContext
import os,json
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
conf=SparkConf().setMaster("local[*]").\
    setAppName("analysis")
conf.set("spark.default.parallelism","1")
sc=SparkContext(conf=conf)
rdd=sc.textFile("search_log.txt")
rdd1=rdd.map(lambda x:x.split("\t"))
#时段搜索榜（top3）
rdd2=rdd1.map(lambda x:(x[0][:2:],1)).reduceByKey(lambda x,y:x+y)#key=time聚合
rdd3=rdd2.sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
print("时段搜索榜（top3）:")
for x in rdd3:
    print(f"时段：{x[0]}点，搜索次数：{x[1]}次")
#搜索词（top3）
rdd4=rdd1.map(lambda x:(x[2],1)).reduceByKey(lambda x,y:x+y)#key=word聚合
rdd5=rdd4.sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
print("搜索词（top3）:")
for x in rdd5:
    print(f"搜索词：{x[0]}，搜索次数：{x[1]}次")
#hadoop时段榜（top3）
rdd6=rdd1.filter(lambda x:x[2]=="hadoop").map(lambda x:(x[0][:2:],1)).reduceByKey(lambda x,y:x+y)
rdd7=rdd6.sortBy(lambda x:x[1],ascending=False,numPartitions=1).take(3)
print("hadoop时段榜（top3）:")
for x in rdd7:
    print(f"时段：{x[0]}点，搜索次数：{x[1]}次")
#转化json数据
rdd8=json.dumps(rdd1.map(lambda x:({"time":x[0],"ID":x[1],"name":x[2],"rank1":x[3],"rank2":x[4],"url":x[5]})).\
                collect(),ensure_ascii=False)
rdd9=sc.parallelize([rdd8])
rdd9.saveAsTextFile("analysis")