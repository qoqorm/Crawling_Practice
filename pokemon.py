import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import os

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://pokemongo.inven.co.kr/dataninfo/pokemon/")
driver.implicitly_wait(10)
sleep(1)

ht = driver.page_source
soup = BeautifulSoup(ht, "html.parser")
driver.close()

if not os.path.isdir("poke"):
    os.mkdir("poke")

for i in soup.select(".pokemonicon"):
    pname = i.select_one("span").text.replace(".", "_")
    link = "https:" + i.select_one("img").get("src").replace("pokemonicon", "pokemonimage")
    r = requests.get(link)
    f = open(f"poke/{pname}.png", "wb")
    f.write(r.content)