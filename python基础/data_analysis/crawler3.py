import urllib
import pandas as pd
import requests
from bs4 import BeautifulSoup
Url = r"https://top.baidu.com/board?tab=realtime"
# hotSearchUrl = r"https://top.baidu.com/board?tab=realtime"
Hot = urllib.request.urlopen(Url).read()
# htmlHotSearch = urllib.request.urlopen(hotSearchUrl).read()
soup1 = BeautifulSoup(Hot, "html.parser")
# soup2 = BeautifulSoup(htmlHotSearch, "html.parser")
hotTitle = soup1.find_all(class_="c-single-text-ellipsis")
hot_title_data = []
for i in hotTitle:
    hot_title_data.append(str(i).split(">")[1].split("<")[0].strip())
HotSearch = soup1.find_all(class_="hot-index_1Bl1a")
HotSearch_data = []
for i in HotSearch:
    HotSearch_data.append(str(i).split(">")[1].split("<")[0].strip())

data = pd.DataFrame({
            "hot_title": hot_title_data,
            "HotSearch_data": HotSearch_data
})
data.to_excel(r"E:\python\file\平德祥.xlsx", index=False)














