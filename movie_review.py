import requests
from bs4 import BeautifulSoup

def delblank(st):
    for i in "\t\n\r":
        st = st.replace(i, "")
    return st
    
for j in range(10):
    res = requests.get(f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=192608&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={j}")
    soup = BeautifulSoup(res.text, "html.parser")

    for i in soup.select("ul > li")[6:]:
        score = delblank(i.select_one("li > .star_score > em").text)
        A = i.select("p > span")
        if len(A) == 2:
            review = delblank(A[1].text)
        else:
            review = delblank(A[0].text)
        ID = delblank( i.select("dt > em")[0].text)
        date = delblank( i.select("dt > em")[1].text)

        print(score ,review, ID, date)


# 평점, 리뷰, ID, 날짜 찾기
