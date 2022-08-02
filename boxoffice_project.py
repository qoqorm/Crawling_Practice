import requests
from bs4 import BeautifulSoup
import os

res = requests.get("https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4")
soup = BeautifulSoup(res.text, "html.parser")

if not os.path.isdir("poster"):
    os.mkdir("poster")


movie_urls = []
for i in soup.select("a.inner")[:10]:
    search_url = "https://search.naver.com/search.naver" + i.get("href")
    res2 = requests.get(search_url)
    soup2 = BeautifulSoup(res2.text, "html.parser")
    movie_url = soup2.select_one(".detail_info > a").get("href")
    movie_urls.append(movie_url)

def filter(st):
    for i in  ':/<\\">|?*':
        st = st.replace(i, "")
    return st

def delblank(st):
    for i in "\t\n\r":
        st = st.replace(i, "")
    return st

for num, k in enumerate(movie_urls, 1):
    res = requests.get(k)
    soup = BeautifulSoup(res.text, "html.parser")

    movie_code = k.split("=")[1]
    poster_url = f"https://movie.naver.com/movie/bi/mi/photoViewPopup.naver?movieCode={movie_code}"
    resp = requests.get(poster_url)
    soup3 = BeautifulSoup(resp.text, "html.parser")
    real_poster_url = soup3.select_one("#targetImage").get("src")
    respo = requests.get(real_poster_url)

    f = open(f"poster/top{num}.png", "wb")
    f.write(respo.content)

    mv_name_kor = soup.select_one(".mv_info_area > .mv_info > .h_movie > a")
    mv_name_eng = soup.select_one(".mv_info_area > .mv_info > strong")

    A = soup.select("dl.info_spec > dd")
    B = A[0].select("span")
    genre = delblank(B[0].text)
    country = delblank(B[1].text)
    mv_time = delblank(B[2].text)
    mv_date = delblank(B[3].text)
    director = A[1].text

    if soup.select_one(".step3"):
        actor = A[2].text.replace("더보기", "")
    else:
        A.insert(2,"")
        actor = "None"

    age_level = delblank(A[3].text)

    if soup.select_one(".step9"):
        audience = A[4].select_one(".count").text
    else:
        audience = "None"

    stars = []
    C = soup.select_one(".main_score")
    if C:
        for i in C.select(".st_on")[:3]:
            a = round(float(i.get("style")[6:-1])/10, 2)
            stars.append(a)
    else:
        stars = ["None"]*3

    # print(mv_name_kor,"\t", mv_name_eng,"\t", genre,"\t", country,"\t", mv_time,"\t", mv_date,"\t", director,"\t", actor,"\t", age_level,"\t", audience,"\t", stars,"\n")


# actor = "None"
# if soup.select_one(".step3"):




# summary = soup.select(".info_spec > dd > p > span > a")
# print(summary[0].text)
# print(summary[1].text)
# mv_time_date = soup.select(".info_spec > dd > p > span ")
# print(mv_time_date)
# mv_time = mv_time_date[2]
# print(mv_time.text)
# mv_date = mv_time_date[3].select("a")[0] + mv_time_date[3].select("a")[1]
# print(mv_date)

# mv_name = filter(mv_info.get(href))





'''
한국어이름
영어이름
장르
나라
상영시간
개봉날짜
감독이름
등급
누적관객
'''