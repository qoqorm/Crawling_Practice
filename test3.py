import requests
from bs4 import BeautifulSoup

for i in range(1, 84):
    res = requests.get(f"https://comic.naver.com/webtoon/detail?titleId=758037&no={i}")
    soup = BeautifulSoup(res.text, "html.parser")

    print(soup.select_one(".view > h3").text)
    print(soup.select_one("#topPointTotalNumber > strong").text)
    print(soup.select_one(".pointTotalPerson > em").text)
    print(soup.select_one(".rt > .date").text)