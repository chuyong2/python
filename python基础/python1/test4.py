import random
"""猜数字游戏
num = 5
if int(input("请猜一个数字：")) == num:
    print("恭喜一次猜对！")
elif int(input("猜错了，再猜一次：")) == num:
    print("猜对了")
else:
    print(f"猜错了 正确数字是%d" % num)
"""

""" 猜数字升级
import random
num = random.randint(1, 10)
guess_num = int(input("输入要猜测的数字:"))
if guess_num == num:
    print("恭喜第一次猜对了！")
else:
    if guess_num > num:
        print("您猜的数字大了")
    else:
        print("您猜的数字小了")

    guess_num = int(input("再次输入你要猜的数字："))

    if guess_num == num:
        print("恭喜猜对了")
    else:
        if guess_num > num:
            print("您猜的数字大了")
        else:
            print("您猜的数字小了")

        guess_num = int(input("最后一次输入你要猜的数字："))

        if guess_num == num:
            print("恭喜最后一次猜对了")
        else:
            print(f"三次机会没有了，没有猜中 正确数字是{num} ")"""

# 猜数字再升级
num = random.randint(1, 100)
flag = True
count = 0
while flag:
    guess_num = int(input("请输入1-100的数字："))
    count += 1
    if guess_num == num:
        print("猜对了")
        break
    else:
        if guess_num > num:
            print("您猜大了")
        else:
            print("您猜小了")
print(f"您总共猜测了{count}次")
