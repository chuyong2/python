import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(1, 5, .2)
y = x * 3 + 5
# 设置中文显示
font = {"family": "SimHei"}
matplotlib.rc("font", **font)
plt.title("pdx的图")
plt.plot(x, y, "r-", x, y + 5, "g--", x, y + 10, "b-.")
plt.show()

x2 = np.arange(1, 6)
y2 = x2 * 3 + 5
x3 = pd.Series(np.arange(60, 80), index=list(map(lambda x: str(x), np.arange(2022120001, 2022120021))))
plt.title("垂直柱形图")
plt.bar(x2, y2, color=["green", "red", "blue", "yellow", "grey"])
plt.xlabel("x的标签")
plt.ylabel("y的标签")
plt.xticks(x2, list("abcde"), rotation=90)
plt.show()

'''plt.bar(x3.index, x3.values)
plt.xticks(x3.index, rotation=90)'''
plt.barh(x3.index, x3.values)
plt.show()

x4 = pd.Series([80, 85, 60, 20, 30], index=list("abcde"))
plt.hist(x4, bins=[20, 50, 60, 90])
plt.show()
