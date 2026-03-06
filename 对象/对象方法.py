class Student():
    name=None,
    birth=None,
    year=None,
    nationality=None
    def age(self):#方法
        Poor=self.year-self.birth
        print(f"{self.name}是{Poor}")
    def age1(self,number):
        print(f"{self.name}是{number(self.year,self.birth)}岁")#外部传入
def age2(a1,a2):
    return a1-a2
STU1=Student()
STU1.name="梦白愿"
STU1.birth=2003
STU1.year=2026
STU1.nationality="中国"
STU2=Student()
STU2.name="梦白愿1"
STU2.birth=2004
STU2.year=2026
STU2.nationality="中国"
STU1.age()
STU2.age()
STU1.age1(age2)
STU2.age1(age2)