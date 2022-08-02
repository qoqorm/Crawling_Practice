import requests
from bs4 import BeautifulSoup
import os
from PIL import Image

# for i in range(100):
#     res = requests.get("https://seoulgallery.co.kr/artist/list?sel_search=&txt_search=&ca_id=66&memid=&page=1")
#     print("/superboard/data/work/thumb2/3529673829_Vfoyck8G_3476dbb5eabfe3c5f2ccd1625d87eb09a6963008.jpg" in res.text)

def filter(st):
    for i in '\r\t\n\\"<>|:?*;/':
        st = st.replace(i, "")
    return st

def makedir(st):
    if not os.path.isdir(st):
        os.mkdir(st)

makedir("gallery")

for page in range(1, 6):
    res = requests.get(f"https://seoulgallery.co.kr/artist/list?sel_search=&txt_search=&ca_id=66&memid=&page={page}")
    soup = BeautifulSoup(res.text, "html.parser")
    for i in soup.select(".itlist2 > li"):
        A = i.select_one(".tmb").get("style").split("'")[1]
        if len(A) == 2:
            사진경로 = "https://wimg.kr/320x250&b=f3f3f3&l=false"
        else:
            사진경로 = "https://seoulgallery.co.kr/" + A
        사진이름 = filter(i.select_one(".it-tit").text)
        r = requests.get(사진경로)
        f = open(f"gallery/{사진이름}.png", "wb")
        f.write(r.content)
        f.close()

        img = Image.open(f"gallery/{사진이름}.png")
        size = img.size
        rate = 500 / size[1]
        img = img.resize((int(size[0]*rate), int(size[1]*rate)))
        img.save(f"gallery/{사진이름}.png")

        





# 서울갤러리 동양화 페이지의 작품 100개 가져와서 저장하기 : https://seoulgallery.co.kr/artist/list?ca_id=66
# 파일 경로
# / 로 시작 : 절대경로
# rootURL 로 부터의 경로 (도메인)
# / 로 시작X : 상대경로
# 마지막 /가 닫힌 지점으로부터의 경로

# -2:44:40 봐야 함 : 이미지 크롤러