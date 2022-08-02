from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests
import os

if not os.path.isdir("LOL"):
    os.mkdir("LOL")

def filter(st):
    for i in "/<>\?\"*:|":
        st = st.replace(i, "")
    return st

driver = webdriver.Chrome("chromedriver.exe")

for k in range(1, 160):
    driver.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={k}")
    driver.implicitly_wait(10)
    sleep(1)
    ht = driver.page_source
    soup = BeautifulSoup(ht, "html.parser")
    champname = soup.select_one(".korName").text.split(",")[0]

    if not os.path.isdir(f"LOL/{champname}"):
        os.mkdir(f"LOL/{champname}")

    links = []
    for i in soup.select(".askin > img"):
        links.append(i.get("src"))

    names = []
    for i in soup.select(".askinname")[::2]:
        names.append(filter(i.text.split("-"[0])))

    for name, link in zip(names, links):
        r = requests.get(link)
        f = open(f"LOL/{champname}/{name}.png", "wb")
        f.write(r.content)