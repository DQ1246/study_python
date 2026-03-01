a=0
b=0
while a<9:
    a+=1
    while b<a:
        b+=1
        print(f"{b}*{a}={a*b}\t",end="")
    b=0
    print("\n")
