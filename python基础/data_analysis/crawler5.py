import re
import pandas as pd
import requests
# from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib

hotGamesUrl = r"https://top.baidu.com/board?tab=game"
htmlGames = urllib.request.urlopen(hotGamesUrl).read()
soup = BeautifulSoup(htmlGames, "html.parser")
hotGamesImg = soup.find_all(class_="img-wrapper_29V76")
nameData = soup.find_all(class_="c-single-text-ellipsis")
# 查看img
Img = [i.img.attrs['src'] for i in hotGamesImg]
Name = [i.text.strip() for i in nameData[::2]]
# 保存图片
for i in range(len(Img)):
    ImgHtml = urllib.request.urlopen(Img[i]).read()
    with open(r'E:\\python\\file\\img' + f'\\{Name[i]}' + ".jpg", "wb+") as f:
        f.write(ImgHtml)
