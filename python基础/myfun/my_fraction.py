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
        for i in range(1, numerator+1):
            if numerator % i == 0 & denominator % i == 0:
                fac = i
            return fr"{int(numerator/fac)}/{int(denominator/fac)}"
    else:
        print("分子需要小于分母！")
        return ""


if __name__ == "__main__":
    print(my_fraction(5, 6))
    print(my_fraction(0, 6))
    print(my_fraction(7, 6))
    print("ok")
