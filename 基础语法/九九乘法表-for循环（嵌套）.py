a=0
b=0
for a in range(1,10):
    for b in range(1,a+1):#range可以用表达式
        print(f"{b}*{a}={a*b}\t",end="")
    print("\n")
