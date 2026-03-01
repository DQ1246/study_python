f=open("练习1.txt",'r',encoding="UTF-8")
a=str(f.readlines())
count=a.count("itheima")
print(f"文件共有{count}个itheima")