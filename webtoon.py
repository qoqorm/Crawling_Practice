import requests
import os
from bs4 import BeautifulSoup

def make_folder(x):
    if os.path.isdir(x):
        pass
    else:
        os.mkdir(x)

def filter(st):
    for i in "/<>\?\"*:|":
        st = st.replace(i, "")
    return st

make_folder("WEBTOON")

date = ["mon", "tue", "wed", "thr", "fri", "sat", "sun"]
for j in date:
    make_folder(f"WEBTOON/{j}")

    res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={j}")
    soup = BeautifulSoup(res.text, "html.parser")

    for i in soup.select(".thumb > a > img"):
        name = filter(i.get("title"))
        link = i.get("src")
        r = requests.get(link)
        f = open(f"WEBTOON/{j}/{name}.png", "wb")
        f.write(r.content)
