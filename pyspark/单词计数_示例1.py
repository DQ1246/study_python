from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
conf=SparkConf().setMaster("local[*]").\
    setAppName("test1")
sc=SparkContext(conf=conf)
rdd=sc.textFile("hello.txt")
rdd1=rdd.flatMap(lambda x:x.split(" "))#分割数据、解套
rdd2=rdd1.map(lambda a:(a,1))#组成二元元组
rdd3=rdd2.reduceByKey(lambda b,c:b+c)#聚合
print(rdd3.collect())
