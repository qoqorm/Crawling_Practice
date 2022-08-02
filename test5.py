import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/weekdayList?week=mon")
soup = BeautifulSoup(res.text, "html.parser")

#t = soup.select(".img_list > li > dl > dt > a".get(""))
# tId = soup.select(".thumb > a").get("href")

# print(tId[0])

for i in soup.select(".thumb > a"):
    print(i.get("title"))
    print(i.get("href"))

    print(i.get("href").split(sep='=')[1].split('&')[0])