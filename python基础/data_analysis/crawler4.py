# 优化+爬图片
# .attrs 返回值为字典，key标签名，value标签值（list） 获取标签内部数据
# .text 获取标签值，返回值字符串
import re
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

MoviesName = [i.text.strip() for i in hotMoviesData1[::2]]
MoviesType = [i.text.strip().replace("类型：", "") for i in hotMoviesData2[::2]]
MoviesActors = [i.text.strip().replace("演员：", "") for i in hotMoviesData2[1::2]]
MoviesIndex = [i.text.strip().strip() for i in hotMoviesData3]
MoviesLink = [str(i).split('href="')[1].split('"')[0] for i in hotMoviesData4]

data = pd.DataFrame({
    "电影名": MoviesName,
    "电影类型": MoviesType,
    "电影演员": MoviesActors,
    "热搜指数": MoviesIndex,
    "电影链接": MoviesLink
})
# data.to_excel(r"E:\python\file\Movies.xlsx", index=False)

# 正则
# 先加载包 规则（我的建议是上网查）需要的字符括号阔住
pattern = re.compile(r'.*?类型：(.*?) .*?')
# re.findall(pattern,string) 返回list
movie_data = [re.findall(pattern, str(i))[0] for i in hotMoviesData2[::2]]
# print(movie_data)

# 爬图片
img-wrapper_29V76






