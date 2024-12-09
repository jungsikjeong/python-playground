import requests
from bs4 import BeautifulSoup

# 해당 데이터를 가져오고
data= requests.get('https://s.search.naver.com/p/review/48/search.naver?ssc=tab.blog.all&api_type=8&query=사과&start=31&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=31&ngn_country=KR&lgl_rcode=09215101&fgn_region=&fgn_city=&lgl_lat=37.560675&lgl_long=127.080038')

# class='\' 껴있는거를 ''로 바꿔주고
soup = BeautifulSoup(data.text.replace('\\',''), 'html.parser')

# 해당 a태그의 class 명 가져오고 (참고로 [] 리스트형식으로 가져옴)
글리스트 =  soup.select('a.title_link')

#출력
print(글리스트[0].text) #겨울홈카페 레시피 사과 계피차 감기에 좋은 차 애플티
print(글리스트[1]['href']) #https://blog.naver.com/puffy38/223686005355
print(글리스트[2].text)






