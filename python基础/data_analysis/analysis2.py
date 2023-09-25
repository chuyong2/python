import os
import pandas as pd
import shutil
os.chdir(r"E:\python\file")

excel_path = os.listdir(os.getcwd())
print(excel_path)

for file_path in excel_path:
    print(pd.read_excel(file_path))

# 删除文件
# os.remove(r"E:\python\file\321.xlsx")

# 移动文件
# shutil.move(r"E:\python\file2\123.xlsx", r"E:\python\file")

''' os.chdir(r"E:\python\file3")
for file_name in os.listdir(os.getcwd()):
    if len(pd.read_excel(file_name)) != 2:
        os.remove(file_name)
        print(f"{file_name}------已删除")'''

# dataframe df = pd.DataFrame(字典， index = 行索引)
d1 = dict(zip(list("abcde"), range(9)))
print(d1)

d2 = {"a": [1, 2, 3], "b": [4, 5, 6]}
print(d2)

df = pd.DataFrame(d1, index=[0, 1, 2])
print(df)
df2 = pd.DataFrame(d2, range(3))
print(df2)







