class clock:
    price=None,
    id=None
    def action(self):#响铃
        import winsound
        winsound.Beep(2000,3000)
clock1=clock()
clock1.price=1999
clock1.id=0
"""class是设计规则，后续基于class（clock）让对象（clock1）干活（赋值，输出等）"""
print(f"编号：{clock1.id}价格：{clock1.price}")
clock1.action()