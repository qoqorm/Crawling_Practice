import requests
from bs4 import BeautifulSoup

def filter(st):
    # 파일이름 설정할 수 없는 것들을 st에서 걸러줌
    # : / < \ " > | ? *
    for i in  ':/<\\">|?*':
        st = st.replace(i, "")
    return st

res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%98%84%EC%9E%AC%EC%83%81%EC%98%81%EC%98%81%ED%99%94")
soup = BeautifulSoup(res.text, "html.parser")

# movies = []

# for i in soup.select(".data_box"):
#     mdetail = []

#     mname = i.select_one("a").text
#     mdetail.append(mname)
#     minfo = i.select(".info_group > dd")
#     for j in minfo:
#         mdetail.append(j.text)

#     movies.append(mdetail)
# print(movies)

for i in soup.select(".data_area"):
    영화제목 = i.select_one(".area_text_box > a").text
    A = i.select(".info_group")
    장르 = "없음"
    상영시간 = "정보없음"

    for j in A[0].select("dd"):
        if j.text[-1] == "분":
            상영시간 = j.text
        else:
            장르 = j.text
    
    개봉날짜 = A[1].select_one("dd").text
    평점 = A[1].select_one(".num").text
    출연자 = A[2].select_one("span").text
    사진경로 = i.select_one("img").get("src")
    r = requests.get(사진경로)
    f = open(f"{filter(영화제목)}.png", "wb")
    f.write(r.content)