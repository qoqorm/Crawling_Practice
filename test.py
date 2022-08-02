import requests
from bs4 import BeautifulSoup

st = """<html>
    <body>
        <div id="hello1">안녕1</div>
        <div class="hello2">안녕2</div>
        <div>
            <span>안녕3</span>
        </div>
        <a href="https://www.naver.com">NAVER</a>
    </body>
</html>"""


res = requests.get("https://comic.naver.com/webtoon/detail?titleId=758037&no=83&weekday=mon")
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select(".view > h3")) 
print(soup.select_one("#topPointTotalNumber > strong"))
print(soup.select(".pointTotalPerson > em"))
print(soup.select(".date"))

res = requests.get("https://comic.naver.com/webtoon/list?titleId=183559")
soup = BeautifulSoup(res.text, "html.parser")

print(soup.select_one("h2 > .title").text)
print(soup.select_one(".wrt_nm").text)
print(soup.select_one(".detail > p").text)
print(soup.select_one(".genre").text)
print(soup.select_one(".age").text)




# # requests.get(url) : rul 로 request 날려준다. response 를 반환
# res = request.get("https://www.naver.com/")
# soup = BeautifulSoup(res.text, "html.parser")
# # s = BeautifulSoup(아무의미없는문자열, "html.parser")
# # 아무 의미 없는 문자열을 HTML 형식으로 해석할 수 있는 s 라는 객체 생성!