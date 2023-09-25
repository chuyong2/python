import re
import fractions
print(str.split("sep"))

print("sep".join(str.split("sep")))

path = r"D:\202206082203.mp4"
print(path.endswith("mp4"))

words = "i love you.you love me"
pattern = "he"
'''print(words.replace("you", "i")) '''
print(re.sub("you", pattern, words))

# pattern正则表达式

print(f"100除3保留三位小数：{round(100/3 , 3)} , 余数：{100%3}")

print(fractions.Fraction(2, 6))

print("1/3")


def my_fraction(numerator, denominator):

    """
    输入分子，分母，进行约分，得到最简分数
    :param numerator: 分子
    :param denominator: 分母
    :return: str，返回最简分数
    """

    if numerator <= denominator:
        '''print("继续")'''
        if numerator == 0:
            print("分子为0")
            return ""
        '''if denominator == 0:
            print("内码，分数定义不知道？")
            return " "'''
        for i in range(1, numerator+1):
            if numerator % i == 0 & denominator % i == 0:
                fac = i
        return fr"{int(numerator/fac)}/{int(denominator/fac)}"
    else:
        print("分子需要小于分母！")
        return ""


print(my_fraction(3, 7))
