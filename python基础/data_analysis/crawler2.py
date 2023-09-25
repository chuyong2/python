import pandas as pd
import requests
# from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import urllib

# 爬百度热搜电影榜
# 电影名，演员，类型，热搜指数
# 存
"""headers = {
    "UserAgent": UserAgent().random
}
"""
hotMoviesUrl = r"https://top.baidu.com/board?tab=movie"
htmlMovies = urllib.request.urlopen(hotMoviesUrl).read()
soup = BeautifulSoup(htmlMovies, "html.parser")
hotMoviesData1 = soup.find_all(class_="c-single-text-ellipsis")
hotMoviesData2 = soup.find_all(class_="intro_1l0wp")
hotMoviesData3 = soup.find_all(class_="hot-index_1Bl1a")
hotMoviesData4 = soup.find_all(class_="title_dIF3B ")

MoviesName = [str(i).split(">")[1].split("<")[0].strip() for i in hotMoviesData1[::2]]
MoviesType = [str(i).split(">")[1].split("<")[0].strip().replace("类型：", "") for i in hotMoviesData2[::2]]
MoviesActors = [str(i).split(">")[1].split("<")[0].strip().replace("演员：", "") for i in hotMoviesData2[1::2]]
MoviesIndex = [str(i).split(">")[1].split("<")[0].strip() for i in hotMoviesData3]
MoviesLink = [str(i).split('href="')[1].split('"')[0] for i in hotMoviesData4]

data = pd.DataFrame({
    "电影名": MoviesName,
    "电影类型": MoviesType,
    "电影演员": MoviesActors,
    "热搜指数": MoviesIndex,
    "电影链接": MoviesLink
})
data.to_excel(r"E:\python\file\Movies.xlsx", index=False)
