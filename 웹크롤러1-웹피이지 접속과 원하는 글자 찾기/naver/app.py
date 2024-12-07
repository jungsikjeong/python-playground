# 파이썬으로 웹사이트 접속 도와주는 라이브러리
import requests
from bs4 import BeautifulSoup

데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')


soup = BeautifulSoup(데이터.content , 'html.parser')
print(soup.find_all('strong',id="_nowVal")[0].text)

print(soup.find_all('span', class_='tah p11')[0].text)

