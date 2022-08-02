import requests
from bs4 import BeautifulSoup

def delblank(st):
    for i in "\t\n\r":
        st = st.replace(i, "")
    return st

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

print("="*30)
print("MELON TOP 10")
print("="*30)
res = requests.get("https://www.melon.com/chart/index.htm", headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
for i in soup.select(".rank01 > span > a")[:10]:
    print(i.text)

print("="*30)
print("GENIE TOP 10")
print("="*30)
res = requests.get("https://www.genie.co.kr/chart/top200", headers=headers)
soup = BeautifulSoup(res.text, "html.parser")
for i in soup.select(".info > .title")[:10]:
    print(i.text.strip())

print("="*30)
print("BUGS TOP 10")
print("="*30)
res = requests.get("https://music.bugs.co.kr/chart")
soup = BeautifulSoup(res.text, "html.parser")
for i in soup.select(".title > a")[:10]:
    print(i.text)
