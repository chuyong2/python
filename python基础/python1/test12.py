# 1
print("map"[::-1])
for i in range(2, -1, -1):
    print(list("map")[i], end="")
print("")
word = list("map")
word.reverse()
for i in word:
    print(i, end="")
print("")
for i in list(reversed(list("map"))):
    print(i, end="")
print("")
# 2
word1 = "py is dai mao"
print(word1.upper())
word1 = "py is dai mao"
print(word1.title())
word1 = "py is dai mao"
print(word1.capitalize())
# 3
a = []
for i in range(1, 101):
    if i % 5 == 0:
        a.append(i)
print(a)
a.sort(reverse=True)
print(a)
print([i for i in range(1, 101) if i % 5 == 0])
# 4
cities = ["suzhou", "shanghai", "hangzhou"]
codes = ["0512", "021", "0571"]
d1 = {}
for i in range(len(cities)):
    d1[cities[i]] = codes[i]
print(d1)

d2 = dict(zip(cities, codes))
print(d2)
# 5
for i in range(97, 123):
    print(chr(i), end=" ")








