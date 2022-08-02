import requests
from bs4 import BeautifulSoup

num = 1

for i in range(1, 11):
    res = requests.get(f"https://news.ycombinator.com/news?p={i}")
    soup = BeautifulSoup(res.text, "html.parser")

    titlelist = soup.select(".titlelink")

    for j in titlelist:
        title = j.text
        print(f"{num}. {title}")
        num += 1