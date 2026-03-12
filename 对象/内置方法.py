class Student():
    name=None,
    number=None
    def __init__(self,name,number):#构造方式，自动运行和传参
        self.name=name
        self.number=number
    def __str__(self):#转化字符串，注释后输出为地址
        return f"类性：{type(self.name)},{self.name},{self.number}"
    def __lt__(self, other):#比较运行算，不能带等号
        return self.number<other.number
    def __le__(self, other):#带等号比较运行算，注释后19~22改变结果
        return self.number <=other.number
    def __eq__(self, other):#等号比较运算，将内存比较转化为变量比较
        return self.number==other.number
STU1=Student("白",1)
STU2=Student("黑",2)
STU3=Student("红",1)
print(STU1)
try:
    print(STU1<=STU3,STU3<=STU1)
except:
    print("__lt__不能比较等于")
print(STU1==STU3,STU1==STU2)