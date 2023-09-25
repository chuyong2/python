import math
import pandas

'''print(f"3.9四舍五入：{round(3.9)}")

print(f"3.1向上取整：{math.ceil(3.1)}")
print(f"3.9向下取整：{math.floor(3.9)}")

print(pandas.Series([222]))'''

# 空字典
d1 = {}

# 空合集
s1 = set()

# 字典 直接创建
'''d2 = {1: "aaa", 2: "bbb", "m": True}
print(d2)'''
# list
'''l1 = [1, 'aaa']'''

# ex
name = ["daimao", "wc", "cao"]
score = [10, 60, 2]
d3 = {}
for i in range(len(name)):
    d3[name[i]] = score[i]

# 字典增删改查
# 增
d3["pingdexiang"] = 100
print(d3, d3["daimao"])
# 改
d3["pingdexiang"] = 20
print(d3, d3["daimao"])
# 删(无返回值)
del d3["pingdexiang"]
print(d3)
# 查
print(list(d3.keys()), d3.values())

print("kk" in d3)

# 元组的解包
name2 = ("lucy", 11, "kwq")
a, b, c = name2
print(a, b, c)

name1 = ["pdx", "nuoNuo", "dyj"]
score1 = [100, 5, 2]
d4 = dict(zip(name1, score1))
print(d4)

d10 = dict(zip(list("abcdefg"), range(10, 16)))
d11 = dict(zip(list("opqrst"), range(1, 6)))
d10.pop("a")
print(d10, d11, d10.get("a", "不存在"))



