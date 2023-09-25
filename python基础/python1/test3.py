# if语句
age = int(input("请输入您的年龄："))
if age >= 18:
    print("您已经成年，游玩需要补票10元")
else:
    print("您未成年，无需补票!")
print("祝您游玩愉快!")

# if...elif...else语句
height = int(input("请输入身高："))
if height < 120:
    print("免费游玩！")
elif height >= 120 & height < 140:
    print("补票五元")
else:
    print("补票十元")
print("祝游玩愉快！")
