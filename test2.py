import requests
from bs4 import BeautifulSoup

a = """
<html>
    <body>
        <div id="hello1" a="b">안녕1</div>
        <div class="hello2" c="d">안녕2</div>
        <div>
            <span loca="seoul">안녕3</span>
        </div>
        <a href="https://www.naver.com">NAVER</a>
    </body>
</html>
"""

soup = BeautifulSoup(a, "html.parser")
print(soup.select_one("#hello1").get("a"))
print(soup.select_one(".hello2").get("c"))
print(soup.select_one("div > span").get("loca"))
print(soup.select_one("a").get("href"))


# li = soup.select("div")

# # print(li)

# for i in li:
#     print(i.text)

# print(soup.select_one("a").text)