# 求1-100的和
'''i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(f"0-100的和为:{sum}")'''

# while 嵌套 （9 9）
'''a = 1
while a <= 9:
    b = 1
    while b <= a:
        print(f"{b} * {a} = { b*a }\t", end="")
        b += 1
    a += 1
    print()
'''
# for循环
'''name = "adhhahduuahdadajsdhasda"
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f"{name}字符串有{count}个a")'''

# for 嵌套
'''for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = { j*i }\t", end="")
    print()'''

# continue停止本次 and break跳出循环
for x in list(range(10, 20, 2)):
    print("111\t", end='')
    continue
    print("222\t", end='')
print()

'''for i in range(1, 3):
    print("111")
    for j in range(1, 4):
        print("222")
        continue
        print("333")
    print("444")'''

for x in range(10, 20, 2):
    print("111\t", end='')
    break
    print("222\t", end='')
