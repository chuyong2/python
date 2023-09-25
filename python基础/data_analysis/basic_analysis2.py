import pandas as pd
import numpy as np

# 数据分析
data = pd.read_excel(r"E:\python\file\analysis\data 2.xlsx")
print(data.head())
# print(data.describe(include="all"))
'''print(data.describe())
print()
column = data.columns'''
# print(column)
# print()

# 查看空值
na_check = data.describe(include='all').loc["count"]
# print(na_check[na_check != len(data)])
# print()

# print(set(data.性别))


# print(data[data.年龄 < 18])

# data.年龄[data.年龄 < 18] = ...  50%分位数
# round(data.年龄.mean())   \\  data.describe().年龄['50%']
# data.年龄[data.年龄 < 18] = round(data.describe().年龄['50%'])

# numpy新建ndarray的基本方法
'''array = np.array(data.年龄[data.年龄 < 18].index) + 1
print(array)'''

# 数据分组  right 默认左开右闭（True）  labels=None,array or False ,default None  bins - 1 = labels数量
# label = ["超过3000","低于3000"]
'''group1 = pd.cut(data.月收入, [min(data.月收入), 3000, max(data.月收入)])
data["月收入分级"] = group1'''

# 查看观点一列数据中最高频次的数据
'''top = data.观点.describe()["top"]
print(top)'''
# 观点一列有问题，填充数据
data = data.fillna(data.观点.describe()["top"])
# 多列
# data.观点 = data.观点.fillna(data.观点.describe()["top"])
# print(data)
'''na_check = data.describe(include='all').loc["count"]
print(na_check[na_check != len(data)])'''

'''Count = len(data.年龄[data.年龄 < 30])
print(Count)'''

data2 = data[1:5]
data3 = data[1195:1199]
print(pd.concat([data2, data3]))
