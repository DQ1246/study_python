from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"]="D:\python\python3.10.11\python.exe"
#创建sparkconf类对象
conf=SparkConf().setMaster("local[*]").\
    setAppName("spark_app")
sc=SparkContext(conf=conf)#基于sparkconf类创建sparkcontext对象
print(sc.version)#版本
sc.stop#停止运行