import random
num = random.randint(1,10)#随机数
a=int(input("第一次："))
if a==num:
    print("猜对了")
else:
    if a>num:
        print("大了")
    else:
        print("小了")
    a=int(input("第二次："))
    if a==num:
        print("猜对了")
    else:
        if a > num:
            print("大了")
        else:
            print("小了")
        if int(input("最后一次"))==num:
            print("猜对了")
        else:
            print("猜错了")