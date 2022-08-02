from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import requests

def filter(st):
    for i in "/<>\?\"*:|":
        st = st.replace(i, "")
    return st

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://lol.inven.co.kr/dataninfo/champion/")
driver.implicitly_wait(10) # 암시적 대기
sleep(1)
ht = driver.page_source

soup = BeautifulSoup(ht, "html.parser")

for i in soup.select(".champImage > a"):
    name = filter(i.get("title"))
    link ="http:" + i.select_one("img").get("src")
    
    r = requests.get(link)
    f = open(f"롤아이콘/{name}.png", "wb")
    f.write(r.content)




# import time
# from unicodedata import name
# from selenium import webdriver

# driver = webdriver.Chrome("chromedriver.exe")

# driver.get("https://www.naver.com")

# # 셀레니움으로 할 수 있는 것들
# # 요소를 지정한 뒤에 값을 넣거나 클릭하거나 값을 읽어올 수 있음
# # 요소.send_keys(value)
# naver_input = driver.find_element_by_css_selector("#query")
# naver_input.send_keys("아리")

# naver_search_button = driver.find_element_by_css_selector("#search_btn > span.ico_search_submit")
# naver_search_button.click()

# img_button = driver.find_element_by_css_selector("#lnb > div.lnb_group > div > ul > li:nth-child(2) > a")
# img_button.click()

# time.sleep(1)

# brwsr_img = driver.find_element_by_css_selector("#main_pack > section.sc_new.sp_nimage._prs_img._imageSearchPC > div > div.photo_group._listGrid > div.photo_tile._grid > div:nth-child(2) > div > div.thumb > a > img")
# brwsr_img.click()

# input()





# # import os
# # import requests
# # from bs4 import BeautifulSoup

# # def make_folder(st):
# #     if os.path.isdir(st):
# #         pass
# #     else:
# #         os.mkdir(st)

# # for i in range(1, 161):
# #     res = requests.get(f"https://lol.inven.co.kr/dataninfo/champion/detail.php?code={i}")
# #     soup = BeautifulSoup(res.text, "html.parser")

# #     print(soup.select("#skinThumbWrap > ul > li > a > img"))

# # img_path = []
# # skin_name = []

# # for i in soup.select(".askin > img"):
# #     img_path.append(i.get("src"))

# # for i in soup.select(".askinname")[::2]:
# #     skin_name.append(i.text[:-7])

