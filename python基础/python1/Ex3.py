import numpy as np
import pandas as pd
import math

a1 = np.arange(2, 11, 2)
# print(a1)
a2 = np.array([[2, 4], [3, 5]])
# print(a2)
a3 = np.array(list(range(3, 7)) * 8).reshape(8, 4)
# print(a3)
a4 = np.zeros((3, 3), dtype=int)
a4[1: 2, :3] = 1
a4[0: 1, :3] = range(4, 7)
# print(a4)

a = np.arange(-1, 4)
b = np.arange(1, 3.5, 0.5)
np.seterr(divide='ignore', invalid='ignore')
'''print(f"b - a:{b - a}")
print(f"a / b:{a / b}")
print(f"b * a:{b * a}")
print(f"(a + b) ^ 2:{np.power((a + b), 2)}")
print(f"(a + 2) / (b - 1):{(a + 2) / (b - 1)}")'''

'''print("sin(b):", np.around(np.sin(b), decimals=3))
print("cos(a):", list(map("{:.3f}".format, np.cos(a))))
c = np.log(a + b)
c[np.isinf(c)] = np.nan
print("ln(a+b):", list(map("{:.2f}".format, c)))'''

'''A = np.array([range(10, 20, 3), range(11, 21, 3), range(12, 22, 3)])
B = np.array([np.linspace(0.1, 0.4, num=4), np.linspace(0.5, 0.8, num=4), np.linspace(0.9, 1.2, num=4)])
print(A)
print(B)'''

'''X1 = np.array([[2, 2, 2, 2], [3, 3, 3, 3]])
X2 = np.zeros((2, 4), dtype=int)
X3 = np.array([[1, 0.1], [2, 0.2], [3, 0.3], [4, 0.4]])
X4 = np.array([[5, -3], [5, -3], [5, -3], [5, -3]])
print(X1)
print(X2)
print(X3)
print(X4)'''

data = pd.read_excel(r"E:\python\实验\实验3data.xlsx")
na_check = data.describe(include='all').loc["count"]
# print(na_check[na_check != len(data)])
# print(data[data.年龄 < 18])
# print(data)

data = data.fillna(data.观点.describe()["top"])
# print(data)
# count = data['性别'].value_counts(ascending=True)
count1 = data['性别'] == '男'
count2 = (data['性别'] == '女')&(data['观点'] == '支持')
print(len(data[count1]))
print(len(data[count2]))
