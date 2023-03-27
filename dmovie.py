# 다음 영화 순위 크롤링 하는 프로그램
# import requests
# from bs4 import BeautifulSoup

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)

# soup = BeautifulSoup(data.text, 'html.parser')
#print(soup)
# 내가 원하는 위치에 있는 데이터 가져오기

'''
여기는 여러줄로 설명할수 있어요
또 써도 되요
'''

#title = soup.select_one('#old_content > table > tbody > tr:nth-child(6) > td.title > div > a')
#print(title.text)

# old_content > table > tbody > tr

# trs = soup.select("#old_content > table > tbody > tr")
# print(trs)

# 랭킹을 달아주기 위한 변수
# rank = 0

# for tr in trs:
	#a_tag = tr.select_one("td.title > div > a")
	# 만약에 a_tag 가 None이 아니면 text를 출력
	#if a_tag is not None:
		#rank = rank + 1
		#print(rank, a_tag.text)


# 다음 영화 순위 크롤링 하는 프로그램
import requests
from bs4 import BeautifulSoup

# 다음 영화 순위 페이지 URL
url = "https://movie.daum.net/ranking/reservation"

# HTTP 요청 보내기
response = requests.get(url)

# HTTP 요청이 성공했는지 확인하기
if response.status_code == 200:
    # HTML 파싱하기
    soup = BeautifulSoup(response.text, "html.parser")
    # 영화 순위 리스트 찾기
    rank = 0
    movie_list = soup.select(".thumb_cont")
    for tr in movie_list:
        rank = rank + 1
        a_tag = tr.select_one("a")
        print(f'{rank}위 {a_tag.text}')
        txt_grade = tr.select_one("span.txt_grade")
        print(f'평점: {txt_grade.text}')
        txt_num = tr.select_one("span.txt_num")
        print(f'예매율: {txt_num.text}')
        txt_date = tr.select_one(".txt_info > span.txt_num")
        print(f'개봉날짜: {txt_date.text}')
else:
    print("HTTP 요청 실패")