from pyspark import SparkConf,SparkContext
#创建sparkconf类对象
conf=SparkConf().setMaster("local[*]").\
    setAppName("spark_app")
sc=SparkContext(conf=conf)#基于sparkconf类创建sparkcontext对象
rdd=sc.parallelize((1,2,3,4,5))
rdd1=sc.parallelize([1,2,3,4,5])
rdd2=sc.parallelize({"key1":"1","key2":"2"})
rdd3=sc.parallelize("abcde")
#数据输出带collect方法
print(rdd.collect())
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
#文件读取
rdd4=sc.textFile("../文件/练习1.txt")
print(rdd4.collect())
sc.stop()
