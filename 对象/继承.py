class a():
    ID=1
    def A_1(self):
        print("封装")
class a1(a):
    IID=a.ID#继承能保留数据也能改变数据，通过父类访问，使用父类数据
    ID=2
    def A1_1(self):
        print("继承")
class a2(a1,a):#多继承：有多个父类，父类呈线性，顺序有误，报错
    def A2(self):
        print("多继承")
A=a()
A1=a1()
A2=a2()
A1.A1_1()
A1.A_1()
print(A.ID)#封装
print(A1.ID)#单继承
print(A1.IID)
print(A2.IID)#多继承
A2.A1_1()
print(f"多继承的{A1.IID}")