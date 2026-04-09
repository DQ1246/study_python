def out(fun):
    def inner():
        print("开始睡觉")
        fun()
        print("起床")
    return inner
@out
def sleep():#传入被@闭包
    import random
    import time
    print("睡眠中……")
    time.sleep(random.randint(1,5))
sleep()#实际是下两行的操作
# a=out(sleep)//一般格式：闭包
# a()