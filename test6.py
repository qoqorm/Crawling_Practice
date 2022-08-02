import requests
from bs4 import BeautifulSoup

date = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

for j in date:
    print(f"\t\t{j}day WEBTOON")
    res = requests.get(f"https://comic.naver.com/webtoon/weekdayList?week={j}")
    soup = BeautifulSoup(res.text, "html.parser")


    #t = soup.select(".img_list > li > dl > dt > a".get(""))
    # tId = soup.select(".thumb > a").get("href")

    # print(tId[0])

    for k, i in enumerate(soup.select(".thumb > a")):
        t = i.get("title")
        tNo = i.get("href").split(sep='=')[1].split('&')[0]
#        print(f"{k}. {t}")
#        print(f"\t {tNo}")

        resd = requests.get(f"https://comic.naver.com/webtoon/list?titleId={tNo}")
        soupd = BeautifulSoup(resd.text, "html.parser")

        print(soupd.select_one("h2 > .title").text)
        print(soupd.select_one(".wrt_nm").text)
        print(soupd.select_one(".detail > p").text)
        print(soupd.select_one(".genre").text)
        print(soupd.select_one(".age").text)


    print("\n\n\n")



