from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
conf=SparkConf().setMaster("local[*]").\
    setAppName("Calculate")
sc=SparkContext(conf=conf)
rdd=sc.parallelize([1,2,3,4,5])
#map#(T)->U//带输入与返回的函数，与rdd的每个数据发生变化，支持链式调用
def func(data):
    return data*2
rdd2=rdd.map(func)
print(f"map:{rdd2.collect()}")
#flatmap//比map多一个嵌套的功能
rdd3=sc.parallelize(["1 2 3","2 3 4"])
rdd4=rdd3.flatMap(lambda x:x.split(" "))
print(f"flatmap:{rdd4.collect()}")
#reducebykey//聚合运算，（v,v）->v
rdd5=sc.parallelize([('黑',1),('黑',2),('白',4),('白',6),('白',8)])
rdd6=rdd5.reduceByKey(lambda a,b:a+b)
print(f"reducebykey:{rdd6.collect()}")
#filter//布尔判断，true保留数据
rdd7=sc.parallelize([1,2,3,4,5])
rdd8=rdd7.filter(lambda x:x%2==0)
print(f"filter:{rdd8.collect()}")
#distinct//去重，无需传参
rdd9=sc.parallelize([1,2,3,2,3,1,6,4,7,6])
rdd10=rdd9.distinct()
print(f"distinct:{rdd10.collect()}")
#sortby//排序
rdd11=sc.textFile("hello.txt")
rdd12=rdd11.flatMap(lambda x:x.split(" "))#分割数据、解套
rdd13=rdd12.map(lambda a:(a,1))#组成二元元组
rdd14=rdd13.reduceByKey(lambda b,c:b+c)#聚合
rdd15=rdd14.sortBy(lambda x:x[1],ascending=False,numPartitions=1)
print(f"soerby:{rdd15.collect()}")
sc.stop()