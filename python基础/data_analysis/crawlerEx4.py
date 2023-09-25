import pandas as pd
from bs4 import BeautifulSoup
import urllib

NovelUrl = r"https://top.baidu.com/board?tab=novel"
htmlNovel = urllib.request.urlopen(NovelUrl).read()
soup = BeautifulSoup(htmlNovel, "html.parser")

hotNovelData1 = soup.find_all(class_="c-single-text-ellipsis")
hotNovelData2 = soup.find_all(class_="intro_1l0wp")
hotNovelData3 = soup.find_all(class_="hot-index_1Bl1a")
# hotNovelData4 = soup.find_all(class_="title_dIF3B ")
hotNovelImgData = soup.find_all(class_="img-wrapper_29V76")

NovelName = [i.text.strip() for i in hotNovelData1[::2]]
NovelAuthor = [i.text.strip().replace("作者：", "") for i in hotNovelData2[::2]]
NovelType = [i.text.strip().replace("类型：", "") for i in hotNovelData2[1::2]]
NovelIndex = [i.text.strip().strip() for i in hotNovelData3]
NovelImg = [i.img.attrs['src'] for i in hotNovelImgData]

for i in range(len(NovelImg)):
    ImgHtml = urllib.request.urlopen(NovelImg[i]).read()
    with open(r'E:\\python\\file\\imgNovel' + f'\\{NovelName[i]}' + ".jpg", "wb+") as f:
        f.write(ImgHtml)
    print(NovelName[i])
data = pd.DataFrame({
    "名称": NovelName,
    "作者": NovelAuthor,
    "类型": NovelType,
    "热搜指数": NovelIndex
})
data.to_excel(r"E:\python\file\baidu_novel.xlsx", index=False)











