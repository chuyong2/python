"""
日期：2022-9-14
内容：
作者：平德祥
a = [1, 23, "xyz", 123]
b = [222, 333, 123, 123]
c = ["oka", True, 123, 231]
b.sort()
print(b)
a.reverse()
print(a)
for i in reversed(a):
    print(i, " ", end="")
print()
print(b.count(123))
print(c.index(231))

data = list(range(5))*5
print(data.index(4))
"""
'''print("{0} and {0}".format("a", 123))
print("{} and {}".format("a", 123))'''

# 1-1000被7整除的数,组成数组
'''a = []
for x in range(1, 1001, 1):
    if x % 7 == 0:
        a.append(x)
print(a)'''

'''b = [i for i in range(7, 1001, 7)]
print(b)'''

a = list(range(10))
'''for t in range(len(a)):
    print(a[t])'''

for x in a:
    print(x)
"""
语法{:格式限定符}
^----居中
<----左对齐
>----右对齐
:----后面填充字符，只能一个字符，若不指定，填充空格
"""
print("{} love {}".format("jack", "rose"))
print("{:^12} love {}".format("jack", "rose"))
print("{:*^12} love {}".format("jack", "rose"))
print("{:@^12} love {}".format("jack", "rose"))
