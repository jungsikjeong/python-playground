from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager

import time


# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://instragram.com') # 이제 원하는 url적으면 파이썬으로 접속해줌

# # 브라우저 유지
# input("Press Enter to close the browser...")  # 엔터 키를 누를 때까지 브라우저 유지


# # 해당 브라우저의 요소 가져오기
# # driver.find_element_by_css_selector('class가 x1lliihq인것')
# time.sleep(2)  # 페이지 로딩 대기

# # 방법 1: 전체 클래스명 사용
# e = driver.find_element(By.CSS_SELECTOR, '.x1lliihq.xlp1vlek.xryxfnj.xln2onr6.x1j0vk5s.xl8bv5gf.xl93l95w.xeugll.x1fj9vlw.xl3faq.be.xlvvkbs.xls928wv.xhkezso.xlwr53x.xlgplm7.xarty.x1943hcx.xllbuxe.xw391rp.xv31lw6.x5n08af.x2buid.xltu3fi.x3x7a5m.xl0wh9bi.xladske.xbvl0k.xl8hxmj')

# # 또는 방법 2: XPath 사용 (텍스트로 찾기)
# e = driver.find_element(By.XPATH, "//*[contains(text(), '앱을 다운로드하세요')]")
# print(e.text)



# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--start-maximized')  # 창 최대화
chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 감지 방지

# 옵션 추가해서 드라이버 시작
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)


driver.get('https://instagram.com')

time.sleep(5)
try:
  id = driver.find_element(By.XPATH, "//input[@aria-label='전화번호, 사용자 이름 또는 이메일']")
  pw = driver.find_element(By.XPATH, "//input[@aria-label='비밀번호']")
  btn = driver.find_element(By.XPATH, "//*[contains(text(), '로그인')]")
  id.send_keys('아이디')  # 해당 요소에 인스타그램 아이디를 적어줌
  pw.send_keys('비번') #해당 요소에 인스타 비번입력
  btn.click()
except Exception as e:
    print("요소를 찾지 못했습니다:", e)

input("Press Enter to close the browser...")