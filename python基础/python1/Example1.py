import random
money = 10000
for i in range(1, 21):
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i},绩效分为{score}，不发工资，下一位")
        continue

    if money >= 1000:
        money -= 1000
        print(f"向员工{i}发放工资1000元，账户余额还剩{money}")
    else:
        print(f"工资发完了，下个月再领吧")
        break

