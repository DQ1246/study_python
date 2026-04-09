from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
conf=SparkConf().setMaster("local[*]").\
    setAppName("test")
sc=SparkContext(conf=conf)
rdd=sc.parallelize([1,2,3,4,5,])
#collect//输出列表
print(f"collect:{rdd.collect()}")
#reduce//聚合，类似于reducebykey，区别：不用关键字
num=rdd.reduce(lambda x,y:x+y)
print(f"reduce:{num}")
#take//取出前n个数据
rdd1=rdd.take(2)
print(f"take:{rdd1}")
#count//数据个数
rdd2=rdd.count()
print(f"count:{rdd2}")