# 인스타 페이지 이동과 이미지 수집

from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager

from dotenv import load_dotenv
import time
import os

load_dotenv()

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

time.sleep(3)
try:
  id = driver.find_element(By.XPATH, "//input[@aria-label='전화번호, 사용자 이름 또는 이메일']")
  pw = driver.find_element(By.XPATH, "//input[@aria-label='비밀번호']")
  btn = driver.find_element(By.XPATH, "//*[contains(text(), '로그인')]")
  id.send_keys(os.getenv('INSTAGRAM_ID'))  # 해당 요소에 인스타그램 아이디를 적어줌
  pw.send_keys(os.getenv('INSTAGRAM_PW')) #해당 요소에 인스타 비번입력
  btn.click()



  time.sleep(3)
  # 페이지이동
  # driver.get('url')을 다음처럼, 한번 더 쓰면 페이지 이동이됌
  driver.get('https://www.instagram.com/katarinabluu/')

  # 첫째사진누름
  # 여러개의 class 명이있지만, 이렇게해도 괜찮은 이유가
  # 수많은 class중에, 맨 첫번째꺼 하나만을 우선으로 가져와서 괜찮음
  driver.implicitly_wait(10) #아래 해당 요소가 안보이면 기다려라는 뜻
  imgEl =driver.find_element(By.CSS_SELECTOR, "div._aagu").click()    

  # 사진저장
  driver.find_element(By.CSS_SELECTOR, "div._aagu").click()    
  # 다음
  # 사진저장
  # 다음
  # ... 계속
  input("Press Enter to close the browser...")

except Exception as e:
    print("오류가 발생했습니다:", e)
    input("Press Enter to close the browser...")  # 오류 발생해도 바로 닫히지 않도록

finally:
    driver.quit() # 브라우저 종료


