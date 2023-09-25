def jc(n):
    if type(n) == str:
        print("请输入正确的阶乘参数进行计算")
        return
    elif n < 0 or type(n) == float:
        print("请输入正确的阶乘参数进行计算")
        return
    elif n == 0 or n == 1:
        return 1
    else:
        j = 1
        for i in range(1, n+1):
            j *= i
        return j


print(jc(4))
jc(4.4)
jc("4.4")
jc(-1)
