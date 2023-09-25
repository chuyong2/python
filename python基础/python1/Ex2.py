# 将整数2016的每一个数字分离出来，依次打印
def depart1(n):
    if n == 0:
        return
    depart1(n // 10)
    print(n % 10, "\t", end="")


# depart1(2016)


def depart2(n):
    if n == 0:
        return
    a = str(n)
    b = []
    for x in a:
        b.append(int(x))
    print(b)


# 创建一个1~1000以内，能被7整除的列表。
def list1():
    a = [i for i in range(7, 1001, 7)]
    print(a)


# list1()


# 将字符串“python”倒着打印输出。输出内容为“nohtyp”
def reverse():
    a = "python"
    b = []
    for i in a:
        b.append(i)
    b.reverse()
    for x in b:
        print(f"{x}", end="")


def reverse2():
    word = "python"
    for i in range(len(word)-1, -1, -1):
        print(word[i], end="")


# reverse2()


# 任意输入两个数，比较大小后，将结果由大至小输出结果。
def compare(a, b):
    if a > b:
        print(f"由大到小排序为：{a}, {b}")
    else:
        print(f"由大到小排序为：{b}, {a}")


# compare(10.092, 10)


# 计算1+2-3+4-5+6-7+8-…的值。
Sum = 0
c = int(input("输入一个整数："))
for i in range(2, c+1):
    if i % 2 == 0:
        Sum += i
    else:
        Sum -= i
print(Sum + 1)


# 打印九九乘法表
def table():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j} * {i} = {i * j}\t", end="")
        print()


table()

