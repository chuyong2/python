def my_out():
    a = input("输入一句话：")
    print(a)


def add1():
    a = int(input("输入一个数字："))
    b = int(input("输入一个数字："))
    print(f"a + b = {a + b}")


def add2(x, y):
    result = x + y
    print(f"x + y = {result}")


def auto_acid(temp):
    print("过站查体温，虹桥火车站")
    # if temp >= 35.6 and temp <= 37.5:
    if 35.6 <= temp <= 37.5:
        print(f"你的温度为{temp}℃，welcome to shanghai!")
    # elif temp > 37.5 and temp < 42:
    elif 37.5 < temp < 42:
        print(f"你的温度为{temp}℃，拖走！")
    else:
        print(f"非人类，请准备战斗！")


def three_num_sum(a, b, c):
    return a + b + c


def Stars(name, *name2):
    print(f"明星1号:{name}")
    for x in range(0, len(name2)):
        print(f"明星{x + 2}号:{name2[x]}")


Stars("蔡徐坤", "薛之谦", "周杰伦")

st = lambda f, g: f * g


def genshin_impact(name1, *name2):
    print(f"{name1}yyds")
    for x in name2:
        print(f"{x}yyds")


genshin_impact("钟离", "甘雨", "爱莉希雅")


def big_dict(key1, value1, *pair):
    d = {key1: value1}
    d.update(dict(pair))
    return d


d = big_dict('a', 888, (555, 333), ('b', 999))
print(d)


def one_s(*parm):
    return parm


parm = one_s("艾米", "琪亚娜")
print(parm)


def two_s(**parm):
    return parm


kk = two_s(钟离=111, 爱莉=123)
print(kk)


def fff():
    x = 2
    y = [3, 4]
    return x, y


print(fff()[1], fff()[0])


print("           i lo ve you     ".strip())





