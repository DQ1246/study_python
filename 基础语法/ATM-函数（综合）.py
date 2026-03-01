money=0
def balance():
    print("------查询余额------")
    print(f"你好，你的余额：{money}")
def increase():
    global money
    a=float(input("输入存款："))
    money+=a
    print("------存款------")
    print(f"梦白愿，你存款：{a}")
    print(f"梦白愿，你余款：{money}")
def decrease():
    global money
    b =float(input("输入取款"))
    if money<b:
        print("余额不足")
    else:
        money-=b
        print("------取款------")
        print(f"梦白愿，你取款：{b}")
        print(f"梦白愿，你余款：{money}")
#running=True//另外一种结束循环
while True:#主函数//另外一种，True换为running=True
    print("--------主菜单--------")
    print("你好，梦白愿，欢迎来到ATM，请选择操作")
    print("查询余额：\t[输入1]")
    print("存款：\t\t[输入2]")
    print("取款：\t\t[输入3]")
    print("退出：\t\t[输入4]")
    cmd=int(input())
    if cmd==1:
        balance()
    elif cmd==2:
        increase()
    elif cmd==3:
        decrease()
    elif cmd==4:
        print("本轮使用完毕")
        break#另外一种：running=False
    else:
        print("无效操作")