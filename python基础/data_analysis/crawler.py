import urllib
from bs4 import BeautifulSoup
import pandas as pd
# 爬虫入门
baidu_hots = r"https://top.baidu.com/board?tab=realtime"

html_baidu = urllib.request.urlopen(baidu_hots).read()
# print(html_baidu)

soup = BeautifulSoup(html_baidu, "html.parser")


# 根据网页标签来获取数据
hot_title = str(soup.find_all(class_="c-single-text-ellipsis")).replace("[", "").replace("]", "")\
    .replace(r'<div class="c-single-text-ellipsis">  ', "")\
    .split(" </div>,")
hot_title[-1] = hot_title[-1].replace(" </div>", "")
hot_title = [i.strip() for i in hot_title]
print(hot_title)
data = pd.DataFrame({"hot_title": hot_title})
data.to_excel(r"E:\python\file\hot_title.xlsx")




