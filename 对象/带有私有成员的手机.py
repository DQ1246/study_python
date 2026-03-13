class phone():
    __is_5g_enable=None
    def __init__(self,is_5g_enable):
        self.__is_5g_enable=is_5g_enable
    def __check_5g(self):#私有保证不方便或不能开放的功能行为
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")
Phone=phone(True)
Phone.call_by_5g()