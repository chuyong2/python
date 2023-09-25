from functools import reduce
lambda a, b: a + b
# reduce(function,sequence)把function作用在sequence上累计计算
print(reduce(lambda a, b: a + b, range(0, 101, 2)))


def f2(n):
    return n % 5 == 0


print(list(filter(f2, range(0, 101))))
# filter(func,s)，func需要计算判断条件，返回true，false
print(list(filter(lambda a: a % 5 == 0, range(0, 101))))


def mu():
    a = int(input("输入正整数以计算其阶乘:"))
    if a < 0:
        return "呆毛"
    if a == 0:
        return f"{a}! = 1"
    muti = 1
    '''for i in range(a, 0, -1):'''
    for i in range(2, a+1):
        muti *= i
    return f"{a}! = {muti}"


# print(mu())


def mu2(n):
    return reduce(lambda a, b: a*b, range(1, n+1))


print(mu2(9))
# map(func,*iterables)
'''print(list(map(lambda a: a*3, [1, 2, 3])))
print(tuple(map(lambda a: a*3, [1, 2, 3])))
print(set(map(lambda a: a*3, [1, 2, 3])))
print(list(map(lambda a, b: a+b, [1, 2, 3], [10, 21, 33])))'''

# 行函数
'''print(dict([(k, j) for k in range(3) for j in range(3, 6)]))'''
# 内置函数 (打开zip可以用list，tuple，set，dic)
'''print(sum([1, 2, 3]))
dd = dict(zip(range(3), range(3, 6)))
print(dd, sum(dd.values()))'''

x = range(1, 4)
'''y = range(4, 7)
z = range(7, 10)
p = zip(x, y, z)
# print(list(p))
u = zip(*p)
print(list(u))
print(list(p))'''


print(list(zip(*[x])))
# enumerate(iterable,start=0)
o = list(range(10, 18))
for i, v in enumerate(o):
    print(i, v)
for i, v in enumerate("ping"):
    print(i, v)
dd = dict(zip("abc", range(3, 6)))
for i, v in enumerate(dd):
    print(i, v)
for i, v in enumerate(dd):
    print(list(dd.values())[i], v)

