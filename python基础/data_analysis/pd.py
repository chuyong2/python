import pandas as pd
import numpy as np

a = pd.Series(range(0, 5), index=list("abcde"))
b = pd.Series(np.arange(0.1, 0.6, 0.1), index=list("abcde"), dtype="int64")
# print(a)
# print(b)

a = a.append(pd.Series(range(0, 5), index=list("fghij")))
# print(a.index)
# ndarray
# print(a.values)
# 可以访问索引值，也可以修改但是只能全部改，不可单个改,但values可以单改
d = pd.Series(np.arange(0, 6))
# print(d.index)
# print(d.values)

'''print(d[[0, 2, 4]])
print(a[["a", "b"]])
print(d.values == 2)
print(d.index[d.values == 2])'''
# ndarray
# print(d.values[d.index == 2])

c = pd.Series(range(0, 5), index=list("abcde"))
c = c.drop("a")
c = c.drop(c.index[1: 3: 1])
# print(c)

e = pd.Series(range(5), list("dkiyb"))
# print(e.reindex(list("kdybie"), fill_value=999))

df = pd.DataFrame({
    "name": ["lily", "lucy", "jack"],
    "age": [19, 25, 35],
    "score": range(90, 93)

})
print(df.head(2))
print()
# series对象
print(df["age"])
print()
print(df[1: 2])
print()
print(df.iloc[0:2, 0:2])
print()
print(df.score)
print()
print(df.at[1, "name"])
print()
print(df.columns)
print()
# 要改全改
print(df[["age", "name"]])
print(df.drop(1, axis=0))
print(df.drop("score", axis=1))
# 既可修改值，也可添加列
df["sex"] = [1, 1, 0]
print()
print(df)
print()
print(df.loc[1])
# 添加行
df.loc[len(df)] = ["daimao", 20, 100, 0]
print()
print(df)

# pd.read_html(io),io为读取网页地址
data = pd.read_html(r"https://wiki.biligame.com/ys/%E7%94%98%E9%9B%A8")
data[5].to_excel(r"E:\python\file\甘雨.xlsx",index=0)





