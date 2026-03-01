f=open("练习2.txt",'r',encoding="UTF-8")#练习2与练习2（txt）都是为该程序服务
with open("练习2（备份）.txt",'w',encoding="UTF-8") as f2:#清空文件，避免程序多次运行，重复结果太多，影响观看
    f2.write("")#可以注释2~4行，随着结果逐步增多，表明程序这次运行
    f2.flush
f1=open("练习2（备份）.txt",'a',encoding="UTF-8")
for line in f:
    a=(str(line).strip().split("，"))
    for x in a:
        if x=="正式":
            f1.write(line)
            f1.flush()
f1.close()
f.close()
print(open("练习2（备份）.txt",'r',encoding="UTF-8").read())



