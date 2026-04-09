def a1(atm_money=0):#外层架构
    def atm(num,a=True):
        nonlocal atm_money#保留修改
        if a:
            atm_money+=num
            print(f"存入：{num},余额：{atm_money}")
        else:
            atm_money -= num
            print(f"取入：{num},余额：{atm_money}")
    return atm
a=a1()
a(1000)
a(100,a=False)