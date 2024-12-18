# 네이버 로그인 캡챠를 우회해보자

1. 네이버 m 로그인 페이지로 이동

> m사이트에서해야 조작이 좀 더 편하다고함 <br/>

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

# 크롬 옵션 설정
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument('--start-maximized')  # 창 최대화
chrome_options.add_argument('--disable-blink-features=AutomationControlled')  # 자동화 감지 방지

# 실제 브라우저처럼 꾸미는 단계로, 내 정보를 가상 크롬 웹에 집어넣는것 <참고1>
# chrome_options.add_argument('user-data-dir=그경로')

# r은 raw string을 의미하며 백슬래시 `\`를 이스케이프 문자로 해석하지않고 문자 그대로 취급해준다다
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


# 네이버 m 로그인페이지 주소
driver.get('https://nid.naver.com/nidlogin.login?realname=Y&type=modal&svctype=262144&returl=https%3A%2F%2Fmy.naver.com')
```

> `참고1` 부분은 크롬 웹에서 url부분에 `chrome://version` 이라고 치면 나오는 사이트에서 `프로필 경로` 라는 부분이 있는데 그걸 복붙하면된다. <br/> > `# 헤더 설정` 부분도 User-Agent부분을 바꿔주면된다. 마찬가지로 `chrome://version`에서 `사용자 에이전트` 라고 적힌 부분을 복붙하자.

위의 코드를 작성하고 실행해주면, `py app.py` 가상 크롬웹에 유저 프로필같은게 나온다.<br/>

![alt text](<스크린샷 2024-12-18 221634.png>)

보이나요? .. 유저 아이콘이?<br/>

2. 아이디와 패스워드 element를 찾아서 입력하자.

- `send_keys`로 아이디와 비밀번호를 각각 입력시키면 되지만, 그럴경우 네이버가 봇으로 판단하여 캡챠를 보여주게된다.

- 복붙으로 아이디/비밀번호를 입력하자.

  - 파이썬으로 복붙하기위해 `pip install pyperclip`로 설치

```python
from selenium.webdriver.common.keys import Keys
import pyperclip

pyperclip.copy(os.getenv('NAVER_ID')) # 아이디 복사


time.sleep(2)

e= driver.find_element(By.CSS_SELECTOR,'#id')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v

time.sleep(1)

pyperclip.copy(os.getenv('NAVER_PW')) # 복사

e= driver.find_element(By.CSS_SELECTOR,'#pw')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v

time.sleep(1)
e.send_keys(Keys.ENTER)
# 프로그램 종료 방지
input('Press Enter to quit')
```

# 요약

- 네이버 m 접속
- 크롬옵션추가
- header도 추가가
- 컨트롤+v로 아이디,비번 입력

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

# 네이버 m 로그인페이지 주소
driver.get('https://nid.naver.com/nidlogin.login?realname=Y&type=modal&svctype=262144&returl=https%3A%2F%2Fmy.naver.com')

time.sleep(2)

pyperclip.copy(os.getenv('NAVER_ID')) # 복사

e= driver.find_element(By.CSS_SELECTOR,'#id')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v

time.sleep(1)

pyperclip.copy(os.getenv('NAVER_PW')) # 복사

e= driver.find_element(By.CSS_SELECTOR,'#pw')
e.send_keys(Keys.CONTROL, 'v') # ctrl+v

time.sleep(1)
e.send_keys(Keys.ENTER)
# 프로그램 종료 방지
input('Press Enter to quit')
```
