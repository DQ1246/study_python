print("欢迎来到游乐园，儿童免费，成人收费")
age=int(input("请输入你的年龄：\n"))
if age>18:
    print("你已成年，需要收费10元")
else:
    print("你未成年，免费游玩")