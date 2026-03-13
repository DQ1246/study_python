class student():
    __name=None
    def __age(self):
        return 123
    def __init__(self,name):
        self.__name=name
    def use(self):#私有成员与方法能被类内部调用
        print(f"{self.__name},{self.__age()}")
STU=student("梦白愿")
try:#对象不能调用私有成员与方法
    print(STU.__name)
except Exception as e:
    print(e)
try:
    print(STU.__age)
except Exception as a:
    print(a)
STU.use()