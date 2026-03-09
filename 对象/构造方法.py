class Student():
    name=None,
    birth=None,
    year=None,
    nationality=None
    def __init__(self,name,birth,year,nationality):#构造方式，自动运行和传参
        self.name=name
        self.year=year
        self.birth=birth
        self.nationality=nationality
        print("证明自动执行")
STU=Student("梦白愿",2003,2026,"中国")
print(STU.__dict__)