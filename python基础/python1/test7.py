"""
日期：2022-9-14
内容：
作者：平德祥
"""
# 列表(什么都可以存,可重复)
a = ["kkk", 123, True]
print(a, '\n', type(a), "\n", len(a))
print("a[0]=", a[0], type(a[0]))
print("列表a的第一个到最后一个序列值为：", a[1:])

# range(start,stop[,step])
# start:起始序列 stop：终止序列（不包括） step：步长
r = range(8)
print(r, type(r))
li = list(range(10))
print(li, type(li), type(li[0]))

# 生成一个0-9的偶数序列
o = list(range(0, 10, 2))
print(o)
# 生成一个0-9的奇数序列
j = list(range(1, 10, 2))
print(j)

# list常用计算操作和函数
x = [111, 222, 333, True]
y = ["xyz", False]
print(x + y, "\n", y + x)
# print(list("abcdefghijklmnopqrstuvwxyz"))

# 切片插值 list[n:n] = [value1, value2, ...]
s = [123, 456, 789]
s[0:0] = ["python"]
print(s)

# 切片删除 负数索引从-1 ~ -无穷
p = list(range(9))
print(p[-1:-4:-1], "\t", end='')
print(f"p[:-1]为：{p[:-1]}")

# append()用于追加元素,extend连接list
s.append(y)
x.extend(y)
print(s, "\n", x)

# insert()
k = [123, "nuo", 987, "pdx"]
k.insert(1, "object")
print(k)

# pop()返回值为删除的值,什么参数都不写返回最后一个元素        del
'''k.pop(1)
print(k)'''
c = k.pop(1)
print(type(c), c)

# remove() 括号里写元素
b = list(range(1, 9, 2))
b.remove(3)
print(b)
