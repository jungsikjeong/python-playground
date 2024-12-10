import time
import requests
from bs4 import BeautifulSoup

# 해당 데이터를 가져오고
# data= requests.get('https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=사과&start=31&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=31&ngn_country=KR&lgl_rcode=09215101&fgn_region=&fgn_city=&lgl_lat=37.560675&lgl_long=127.080038')

# class='\' 껴있는거를 ''로 바꿔주고
# soup = BeautifulSoup(data.text.replace('\\',''), 'html.parser')

# 해당 a태그의 class 명 가져오고 (참고로 [] 리스트형식으로 가져옴)
# 글리스트 =  soup.select('a.title_link')

#출력
# print(글리스트[0].text) #겨울홈카페 레시피 사과 계피차 감기에 좋은 차 애플티
# print(글리스트[1]['href']) #https://blog.naver.com/puffy38/223686005355
# print(글리스트[2].text)



# TODO:
data = requests.get('https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=%EA%B0%95%ED%95%B4%EB%A6%B0&start=31&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=11245103&fgn_region=&fgn_city=&lgl_lat=37.530797&lgl_long=126.729707&enlu_query=IggCAP6CULgjAAAAuGDqbIuW1YP0vEg6kPSZvC4UrJY3AOnJda5G7RpKebX0MAbJjXuPJdeUUmtnzJSpj5OKFELyJ9a63EqVpJNsKs80EOg61JxSPuc6IOec3bYFeP3l6j%2FEr50qni1pK6jXT3%2BYTMlUbVvXtIjG%2Fwduedkr0m2YPSvphNE9SM3FlJnW36DeaIVGqNaAWvA%2F3BDJFH2oiiyh6lPoW6xpsVsYHDL13CFRi1fnUHgHW8zN4Y0Nssf4DhkExp6T%2FhMrypBUAulvS%2Bcrmb7mzJTi%2FbXwjAF7p8eeJz%2FYK53XZsz4Q2I%3D&enqx_theme=IggCAGmCULibAAAAh%2FDtntZaiMLGh3DOFtIyqym6fZamxg6or%2F3%2B%2FddkYDmsVA7yJ4hAgQoGBrpz2Ev9vhKpkkv8o9qEZsWh3Dn8U2SyU%2B%2FwMdOQJsYdd8Y7Hi0%3D&abt=&retry_count=0')
soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
list=soup.select('div.title_area a.title_link')


def 강해린정보출력함수(start=31):
  data = requests.get(f'https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=%EA%B0%95%ED%95%B4%EB%A6%B0&start={start}&nx_search_query=&nx_and_query=&nx_sub_query=&ac=0&aq=0&spq=0&sm=tab_hty.top&nso=&prank=30&ngn_country=KR&lgl_rcode=11245103&fgn_region=&fgn_city=&lgl_lat=37.530797&lgl_long=126.729707&enlu_query=IggCAP6CULgjAAAAuGDqbIuW1YP0vEg6kPSZvC4UrJY3AOnJda5G7RpKebX0MAbJjXuPJdeUUmtnzJSpj5OKFELyJ9a63EqVpJNsKs80EOg61JxSPuc6IOec3bYFeP3l6j%2FEr50qni1pK6jXT3%2BYTMlUbVvXtIjG%2Fwduedkr0m2YPSvphNE9SM3FlJnW36DeaIVGqNaAWvA%2F3BDJFH2oiiyh6lPoW6xpsVsYHDL13CFRi1fnUHgHW8zN4Y0Nssf4DhkExp6T%2FhMrypBUAulvS%2Bcrmb7mzJTi%2FbXwjAF7p8eeJz%2FYK53XZsz4Q2I%3D&enqx_theme=IggCAGmCULibAAAAh%2FDtntZaiMLGh3DOFtIyqym6fZamxg6or%2F3%2B%2FddkYDmsVA7yJ4hAgQoGBrpz2Ev9vhKpkkv8o9qEZsWh3Dn8U2SyU%2B%2FwMdOQJsYdd8Y7Hi0%3D&abt=&retry_count=0')
  soup = BeautifulSoup(data.text.replace('\\',''),'html.parser')
  list= soup.select('div.title_area a.title_link')
  img_list = soup.select('div.mod_ugc_thumb_area img')

  for item, img in zip(list, img_list):
    print(img['src'])  # 이미지 URL
    print(item['href'])  # 링크
    print(item.text)  # 제목
    print("-" * 50)  # 구분선


start = 31
while True:
  result = 강해린정보출력함수(start)
  if not result:
    break
  start+=31
  time.sleep(1)

  






