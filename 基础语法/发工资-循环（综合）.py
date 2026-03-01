import random
a=0
b=10000
for a in range(1,21):
    num = random.randint(1, 10)
    if num>5:
        print(f"员工{a}发放1000元，账户余额：{b - 1000}元")
        b -= 1000
        if b == 0:
            break
        continue
    print(f"员工{a}，绩效分：{num}，低于5，不发工资，下一位")