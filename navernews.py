import requests
from bs4 import BeautifulSoup

def delblank(st):
    for i in "\t\n\r":
        st = st.replace(i, "")
    return st

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

for date in range(1, 31):
    res = requests.get(f"https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid2=732&sid1=105&date=202206{str(date).zfill(2)}", headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    for i in soup.select(".list_body > ul > li"):
        A = i.select("dt > a")

        if len(A) == 2:
            A.pop(0)
        print(delblank(A[0].text))


# 문자열.zfill(x)
# 문자열이 x 칸을 채우지 못하면 0 으로 채워줌
# 01 ~ 24
# "1".zfill(2)
# 01
# "1".zfill(3)
# 001

