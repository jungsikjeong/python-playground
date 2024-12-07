import requests
from bs4 import BeautifulSoup

데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')


soup = BeautifulSoup(데이터.content , 'html.parser')
print(soup.find_all('em',class_="no_up")[0].text)


