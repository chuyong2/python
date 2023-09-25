# 1、输入两个数，如a=3，b=2，要求将a和b的值调换，并打印出结果。
"""print("请输入两个数：")
a = int(input("第一个数a："))
b = int(input("第二个数b："))
a, b = b, a
print(f"a变换后为：{a}")
print(f"b变换后为：{b}")"""


# 2、将已知字符串“love python forever”中的每一个字母以大写字母形式输出。
"""x = "love python forever"
y = x.upper()
print(y)"""


# 3、用print函数将“明月几时有”和“把酒问青天”两句话分两行输入，但输出结果在同一行。
"""print("请输入明月几时有，把酒问青天（分两行输入）：")
a = input()
b = input()
print(f"{a},{b}", end='')"""


# 4、生成一个列表a，其中元素为1-100以内的奇数，打印输出结果。
"""num = 0
for a in list(range(1, 100, 2)):
    print(a, "\t", end="")
    num += 1
    if num % 5 == 0:
        print()"""


# 5、生成一个由100以内能被5整除的数组成的数组。
"""b = []
for a in list(range(100)):
    if a % 5 == 0:
        b.append(a)
print(b)"""


# 6、让用户输入一个词，并显示这个词的长度。
"""name = input("请输入一个词:")
print(f"您输入的词为：{name}\n您输入词的长度为：{len(name)}")"""


# 7、生成一个字符串列表，其中元素为字母a~g，如[‘a’，‘b’，‘c’，….,‘g’]，打印结果。
"""print(list("abcdefg"))"""

# 8、制作一个简易两个数求和计算器，能够输入两个数以后，输出两个数求和的计算结果。
"""print("欢迎来到两数求和计算器小程序")
a = int(input("请输入第一个数:"))
b = int(input("请输入第二个数:"))
print(f"两数之和为：{a + b}")"""


