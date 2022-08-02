from bs4 import BeautifulSoup, BeautifulStoneSoup
from selenium import webdriver
import requests
from time import sleep
from bs4 import BeautifulSoup
import os

def filter(st):
    for i in '"/\:<>|>*':
        st = st.replace(i, "")
    return st

def makedir(st):
    if not os.path.isdir(st):
        os.mkdir(st)

makedir("가사모음집")

artist = input("artist search : ")

driver = webdriver.Chrome("chromedriver.exe")
driver.get(f"https://vibe.naver.com/search?query={artist}")
sleep(1)
ht = driver.page_source
soup = BeautifulSoup(ht, "html.parser")
artist_no = soup.select_one(".popular_item").get("href")
artist_name = soup.select_one(".title > div.text").text

makedir(f"가사모음집/{artist_name}")


driver.get(f"https://vibe.naver.com{artist_no}/albums")
driver.implicitly_wait(10)
sleep(1)
ht = driver.page_source
soup = BeautifulSoup(ht, "html.parser")

for i in soup.select(".naver-splugin"):
    album_name = filter(i.get("data-title"))
    album_link = i.get("data-url")
    print(album_name, album_link)

    makedir(f"가사모음집/{artist_name}/{filter(album_name)}")

    driver.get(album_link)
    driver.implicitly_wait(10)
    sleep(1)
    ht = driver.page_source
    soup = BeautifulSoup(ht, "html.parser")

    for i in soup.select(".inner_cell > a"):
        song_link = i.get("href")
        song_title = filter(i.text)

        res = requests.get(f"https://apis.naver.com/vibeWeb/musicapiweb{song_link}/info")

        # 가사가 없는 경우도 있음
        if "<![CDATA[N]]>" in res.text:
            continue
        lyric = res.text.split("<lyric><![CDATA[")[1].split("]]></")[0]
        f = open(f"가사모음집/{artist_name}/{album_name}/{song_title}.txt", "w", encoding="utf-8")
        f.write(lyric)
        f.close()




# 프로그램 잡을 때 작게작게 해서 만들기!!



# F12 -> 네트워크 -> info를 들어감 -> requests로 가능
# import requests

# for i in range(1000):
#     res = requests.get("https://apis.naver.com/vibeWeb/musicapiweb/track/50800359/info")
#     print("포식자\n봐봐" in res.text)