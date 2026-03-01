def evidence(a):
    if a>24:
        print("请提供最新的24h证明")
    elif 0<a<=24:
        print("证明正常")
b=0
print("欢迎来到梦白愿")
b=int(input("输入证明时效"))
evidence(b)