import pandas as pd
import numpy as np

dataframe = pd.DataFrame({
    "name": ["lily", "lucy", "jack", "rose"],
    "age": np.arange(22, 22 + 4),
    "score": (22, 33, 44, 55)
}, index=list(map(lambda x: "202012000" + str(x), range(1, 5))))
# ["202012000" + str(i) for i in range(1, 5)]
# 查学号为2020120002
# dataframe["name"] -> series,dataframe[["name"]] ->dataframe
'''print(dataframe[dataframe.index == "2020120002"])
print()
print(dataframe.loc["2020120002"])'''

# 拼接DataFrame
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list("ab"))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list("ab"))
# print(df1.append(df2, ignore_index=True))

# 数据分析
data = pd.read_excel(r"E:\python\file\analysis\data.xlsx")
# print(data.head())
# print(data[data.G == 1])
# print(data[data.CF_TD.between(0, 0.1)])
# count:计数 mean:平均值 std:标准差 min:最小值 25%:25%分位数 max:最大值
print(data.describe())







