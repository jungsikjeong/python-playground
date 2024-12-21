from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service  
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options
import time
import pyperclip
import os

from dotenv import load_dotenv

load_dotenv()


# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--start-maximized')  # 창 최대화
chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 감지 방지

chrome_options.add_argument(r'user-data-dir=C:\Users\wndtl\AppData\Local\Google\Chrome\User Data\Profile 1')

# 옵션 추가해서 드라이버 시작
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=chrome_options
)


# 헤더 설정
driver.execute_cdp_cmd('Network.setExtraHTTPHeaders', {
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
    }
})

# 네이버 로그인페이지 주소
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/')

time.sleep(2)

# 아이디 복사붙여넣기
pyperclip.copy(os.getenv('NAVER_ID')) # 복사
e= driver.find_element(By.CSS_SELECTOR,'#id')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v 

time.sleep(1)

# 비밀번호 복사 붙여넣기
pyperclip.copy(os.getenv('NAVER_PW')) # 복사
e= driver.find_element(By.CSS_SELECTOR,'#pw')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v 

time.sleep(1)
# 엔터(로그인)
e.send_keys(Keys.ENTER)

time.sleep(2)

# ( 네이버 글쓰기메뉴리스트 펼치기)
e=driver.find_elements(By.CSS_SELECTOR,'ul.MyView-module__menu_list___UzzwA li.MyView-module__menu_item___zAxPt')[2].click()

time.sleep(1)

# 네이버 글쓰기 페이지로 이동
e=driver.find_element(By.CSS_SELECTOR,'div.MyView-module__sub_right___NNT0B').click()

try:
    # 페이지 로드 대기
    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script('return document.readyState') == 'complete'
    )

    time.sleep(3)
    
    # iframe이 존재하는지 먼저 확인
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    print(f"발견된 iframe 개수: {len(iframes)}")
    
    for idx, iframe in enumerate(iframes):
        try:
            iframe_id = iframe.get_attribute('id')
            print(f"iframe {idx}: id = {iframe_id}")
        except:
            print(f"iframe {idx}: id 속성을 가져올 수 없음")

    # my-iframe으로 전환 시도
    iframe_el = driver.find_element(By.ID, "my-iframe")
    driver.switch_to.frame(iframe_el)

    # iframe 안의 엘리먼트 찾기
    e=driver.find_element(By.CSS_SELECTOR, "div#SE-49f313b240-968b-4fa6-92e9-e79eb7c4652b") 

    # 텍스트 입력
    e.send_keys('제목입니다')

except Exception as e:
    print(f"오류 발생: {e}")

time.sleep(1)
# 프로그램 종료 방지
input('Press Enter to quit')