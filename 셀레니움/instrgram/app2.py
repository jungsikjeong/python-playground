# 인스타 로그인

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

time.sleep(5)
try:
  id = driver.find_element(By.XPATH, "//input[@aria-label='전화번호, 사용자 이름 또는 이메일']")
  pw = driver.find_element(By.XPATH, "//input[@aria-label='비밀번호']")
  btn = driver.find_element(By.XPATH, "//*[contains(text(), '로그인')]")
  id.send_keys(os.getenv('INSTAGRAM_ID'))  # 해당 요소에 인스타그램 아이디를 적어줌
  pw.send_keys(os.getenv('INSTAGRAM_PW')) #해당 요소에 인스타 비번입력
  btn.click()
except Exception as e:
    print("요소를 찾지 못했습니다:", e)

input("Press Enter to close the browser...")