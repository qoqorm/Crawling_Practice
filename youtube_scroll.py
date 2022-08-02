from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=90oSCV8gMsg&ab_channel=%EC%98%A4%ED%94%88%ED%82%A4%EC%B9%9COpenKitchen")

BFscroll = driver.execute_script("return document.documentElement.scrollHeight;")

while True:
    driver.execute_script("scrollTo(0, document.documentElement.scrollHeight);")
    sleep(1)
    AFTscroll = driver.execute_script("return document.documentElement.scrollHeight;")
    if BFscroll == AFTscroll:
        break
    BFscroll = AFTscroll

ht = driver.page_source
soup = BeautifulSoup(ht, "html.parser")

for i in soup.select("div#main"):
    작성자 = i.select_one("#author-text > span").text.strip()
    댓글내용 = i.select_one("#content-text").text
    일시 = i.select_one(".published-time-text > a").text
    좋아요 = i.select_one("#vote-count-middle").text.strip()
    print(f"{일시} {작성자} 님의 댓글내용 좋아요 {좋아요}")
    print("="*30)
    print(댓글내용)
    print()
    print()
    
