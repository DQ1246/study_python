class Student():#1、创建类
    name=None,
    age=None,
    gender=None,
    nationality=None
STU=Student()#2、创建对象
STU.name="梦白愿"#3、对对象赋值
STU.age=20
STU.gender="男"
STU.nationality="中国"
print(STU.name)#输出单个属性
print(STU.__dict__)#输出全局内容
