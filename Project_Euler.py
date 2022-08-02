import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"}

# for i in range(100):
#     res = requests.get("https://euler.synap.co.kr/prob_list.php")
#     print("수열에서 4백만 이하이면서 짝수인 항의 합" in res.text)

driver = webdriver.Chrome("chromedriver.exe")

for k in range(1, 20):
    driver.get(f"https://euler.synap.co.kr/prob_list.php?pg={k}")
    # res = requests.get("https://euler.synap.co.kr/prob_list.php", headers=headers)
    sleep(2)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    for i in soup.select(".grid > tbody > tr")[2:]:
        A = i.select_one("a")
        prob_name = A.text
        prob_level = A.get("title").split("x")[0]
        prov_solver = i.select("td")[3].text.strip()



# 브라우저가 뼈대를 만들어 버려서 
# table > tr 하면 잘 나올 것이지만
# tbody 는 브라우저가 만든 것이라 안 나옴
# 개발자가 만들지 않은 것들은 나오지 않음!!!