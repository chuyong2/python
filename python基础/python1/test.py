# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = 100
print(a + 50)

# 同种类型可直接拼接
b = "hello"
c = "world!!!!"
print(b + c + "哈哈")

# 不同类型用，隔开来拼接
d = 50
print("钱包还有：", d)

# 输出类型
print(type("hello"))
print(type(2))
print(type(2.1))

money = 100
type_name = type(money)
print(type_name)

# 类型转换
k = str(111)
print(type(k), k)

num = int("123")
print(type(num), num)

name2 = "\"我是"
name = "\"呆毛\""
print(name2 + '  ' + name)

# 股价计算小程序
name3 = "传智播客"  # 公司名
stockPrice = 19.99  # 当前股价
stockCode = "003032"  # 股票代码
stockPriceDailyGrowthFactor = 1.2 # 股票价格每日增长因子
growthDays = 7   # 增长天数
finallyStockPrice = stockPrice * stockPriceDailyGrowthFactor ** growthDays
print(f"公司：{name3},股票代码:{stockCode},当前股价:{stockPrice}")
print("每日增长系数 %.1f,经过%d天的增长后，股价达到了：%.2f"
      % (stockPriceDailyGrowthFactor, growthDays, finallyStockPrice))


# 数据输入
print("请输入您的姓名:")
name4 = input()  # name4 = input("请输入您的姓名:") input()默认为字符串
print("ok,i know your name is %s" % name4)

num2 = int(input("密码："))
print("我知道了！是%d" % num2, type(num2))


























