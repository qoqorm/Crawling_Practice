import requests
from bs4 import BeautifulSoup

def delblank(st):
    for i in "\t\n\r":
        st = st.replace(i, "")
    return st

res = requests.get(f"https://movie.naver.com/movie/bi/mi/script.naver?code=192608&order=best&nid=&page=1")
soup = BeautifulSoup(res.text, "html.parser")

total = int(soup.select_one(".cnt > em").text)
total_page = total // 10 + 1

for j in range(1, total_page+1):
    res = requests.get(f"https://movie.naver.com/movie/bi/mi/script.naver?code=192608&order=best&nid=&page={j}")
    soup = BeautifulSoup(res.text, "html.parser")
    
    for i in soup.select("ul > li")[4:]:
        one_line = delblank(i.select(".one_line")[0].text)
        char_part = delblank(i.select_one(".char_part > span").text)
        actor = delblank(i.select_one(".char_part > a").text)
        id = delblank(i.select_one("span > a").text)
        recomm = delblank(i.select_one(".w_recomm > em").text)
        date = delblank(i.select_one(".date").text)

        print(one_line ,char_part, actor, id, recomm, date)


# 명대사 긁어오기







