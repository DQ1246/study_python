class a:#顶层与具象类
    pass
class b(a):
    pass
class c(a):
    pass
class d(a):
    pass
class factory:#工厂，选择类
    def get_factory(self,x):
        if x=="b":
            return b()
        elif x=="c":
            return c()
        elif x=="d":
            return d()
Factory=factory()
b=Factory.get_factory('b')
c=Factory.get_factory('c')
d=Factory.get_factory('d')
print(b)
print(c)
print(d)


