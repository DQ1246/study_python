num=10#目标数字
if int(input("请输入第一次猜的数字："))==num:
    print("猜对了")
elif int(input("再猜一次："))==num:
    print("猜对了")
elif int(input("最后一次："))==num:
    print("猜对了")
else:
    print("全部猜错了，目标数：%d"%num)

