import requests

headers ={
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

cookie = {'ad-id': 'A9sVvHK15UUkjz8Vxh40zgQ', 'ad-privacy': '0'}

r = requests.get('https://www.amazon.com/ref=cs_503_logo',headers=headers,cookies=cookie)

from bs4 import BeautifulSoup
soup= BeautifulSoup(r.content,'lxml')


try:
  print(soup.select('.a-size.medium')[110]) # 이거해보고 
except:
  print('안되네요') # 혹시 에러뜨면 이거


# if r.status_code == 200:
  # soup= BeautifulSoup(r.content,'lxml')
  # print(soup.select('.a-size.medium')[0])
# else :
#   print('에러났어요')


# print(r.content)
# print(r.status_code)


