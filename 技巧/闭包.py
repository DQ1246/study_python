def a(a1):
    def b(b1):
        print(f"{a1}-{b1}-{a1}")
    return b
x=a("白")#确定外框架{白}-{b1}-{白}
x("黑")#确定内框架{白}-{黑}-{白}
