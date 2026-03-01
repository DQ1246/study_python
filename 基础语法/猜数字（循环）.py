import random
num = random.randint(1,100)#随机数
a=0
count=1
a=int(input("输入数字："))
while a!=num:#直接用bool判断，后面在改为False就行
    count+=1
    if a>num:
        print("大了")
    else:
        print("小了")
    a=int(input("重新来一次："))
print("猜对了，目标数：%d，你一共猜了：%d次"%(num,count))