from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
conf=SparkConf().setMaster("local[*]").\
    setAppName("test")
#conf.set("spark.default.parallelism","1")//方法1
sc=SparkContext(conf=conf)
rdd=sc.parallelize([1,2,3,4,5],1)#方法2，分区数
rdd.saveAsTextFile("E:\桌面\练习\python\pyspark/test1")
sc.stop()
