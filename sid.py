import requests
from bs4 import BeautifulSoup

cookies = {"sid" : "B2A0F56E-46B3-413C-AEBB-1CE013F9C1BE"}
res = requests.get(f"https://mgr.kgitbank.com/board.it?db=student_notice", cookies=cookies)
res.encoding = "utf-8"
soup = BeautifulSoup(res.text, "html.parser")

for i in soup.select(".table-bordered > tr")[1:]:
    print(i.select("td")[1].text)





# Application -> Cookies -> 밑에 사이트 클릭 -> sid/user/name 중에 sid 의 value 값 가져가기 (신분증)
# 세션 id 는 로그아웃하면 끊김
# 로그인을 하면 또 달라짐

# encoding 바꾸는 방법
# res.encoding = "utf-8"

