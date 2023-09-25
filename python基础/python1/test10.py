"""
date:2022-10-13
content:
1.复习
2.字典
"""

a = list("abcdabababcdcdcdab")
print(f"list(a):{a}")
b = set(a)
print(f"set(b):{b}")

print('a' in b)
b.add("element")
print(f"set(b) after:{b}")

# 集合运算
'''c = list("abc") + list("abc")
print(c)
d = list("abc") * 9
print(d)'''
c = set("abcdefg")
d = set("apple")
print(c - d)
print(c | d)
print(c & d)
print(c ^ d)






