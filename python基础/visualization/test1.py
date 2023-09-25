import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import re

'''height = [160, 170, 180, 190, 200]
weight = [50, 51, 52, 53, 54]
plt.scatter(height, weight)
plt.show()'''
# data = pd.read_excel(r"E:\python\file\analysis\data3.xlsx")
data = pd.read_clipboard()
print(data.head())
data2 = "2018年末，东部地区拥有法人单位1280.2万个，占58.8%，比2013年末下降了0.5个百分点；" \
        "中部地区492.9万个，占22.6%，提高了0.1个百分点；" \
        "西部地区405.8万个，占18.6%，提高了0.4个百分点。" \
        "东部地区拥有产业活动单位1408.3万个，占57.4%；" \
        "中部地区568.4万个，占23.2%；" \
        "西部地区478.3万个，占19.5%。 "
print(data2)
pattern = re.compile(r".*?法人单位(.*?)万个.*?地区(.*?)万个.*?地区(.*?)万个.*?")
num_data = re.findall(pattern, data2)[0]
num_data = list(map(lambda x: float(x), num_data))
