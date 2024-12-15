# TODO: 문제풀이
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
from datetime import datetime

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
  pw.send_keys(os.getenv('INSTAGRAM_PW')) # 해당 요소에 인스타 비번입력
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
  
  def isVideo():
        try:
            video = driver.find_element(By.CSS_SELECTOR, "video.x1lliihq.x5yr21d.xh8yej3")
            return video.get_attribute('src') is not None
        except:
            return False

  def downloadVideo(post_num):
        try:
            video = driver.find_element(By.CSS_SELECTOR, "video.x1lliihq.x5yr21d.xh8yej3")
            videoSrc = video.get_attribute('src')
            
            if not videoSrc:
                print("비디오 소스를 찾을 수 없습니다.")
                return
                
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            urllib.request.urlretrieve(videoSrc, f'video_{current_time}_{post_num}.mp4')
            print(f"비디오 다운로드 완료: video_{current_time}_{post_num}.mp4")

        except NoSuchElementException:
            print("비디오 요소를 찾을 수 없습니다.")
        except Exception as e:
            print(f"비디오 다운로드 중 오류 발생: {str(e)}")

  def downloadImg(post_num):
    try:
        if isVideo():
            downloadVideo(post_num)
            return # 비디오면 이미지 다운로드 건너뛰기
        
        isMultiple = driver.find_elements(By.CSS_SELECTOR, "div.x1qjc9v5 button._afxw")
        # 한 게시글에 여러 사진이있다면
        if isMultiple:
           img_count = 0  # 각 게시물 내의 이미지 카운터
           while True:
            try: 
                # 현재 보이는 이미지 다운로드
                all_images = driver.find_elements(By.CSS_SELECTOR, "li._acaz div._aagv img")
                current_img = all_images[img_count]
                
                # current_img = driver.find_element(By.CSS_SELECTOR, "div._aagv img")
                imgURL = current_img.get_attribute('src')    
                urllib.request.urlretrieve(imgURL, f'{post_num}_{img_count + 1}.jpg')
                    
                # 다음 버튼 클릭
                next_button = driver.find_element(By.CSS_SELECTOR, "div.x1qjc9v5 button._afxw")
                next_button.click()
                    
                # 잠시 대기 (이미지 로딩을 위해)
                time.sleep(1)
                img_count += 1

            except Exception as e:
                # 더 이상 다음 이미지가 없으면 종료
                print(f"포스트 {i}의 모든 이미지 다운로드 완료")
                break
        
        # 한 게시글에 사진이 한장뿐이라면
        if not isMultiple:
            imgURL= driver.find_elements(By.CSS_SELECTOR, "div._aagv img")[0].get_attribute('src')    
            urllib.request.urlretrieve(imgURL, f'{i}.jpg')
            return 
    except Exception as e:
        print(f"오류가 발생했습니다: {str(e)}")

  def clickNextBtn():
      driver.find_element(By.CSS_SELECTOR, 'button._abl-').click()
      time.sleep(1)

  for i in range(20):
    time.sleep(1)
    downloadImg(i)
    time.sleep(1)
    clickNextBtn()
    
  input("Press Enter to close the browser...")

except Exception as e:
    print("오류가 발생했습니다:", e)
    input("Press Enter to close the browser...")  # 오류 발생해도 바로 닫히지 않도록

finally:
    driver.quit() # 브라우저 종료


# TODO: 댓글달기,좋아요누르기

