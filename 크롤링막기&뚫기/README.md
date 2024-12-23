## 방법1:user-agent 생성

- f12-네트워크-Request Headers/ `user-agent`
  - 나의 os상태를 보여줌 (윈도우,맥북,크롬브라우저 정보등등)
  - 파이썬으로 접속이안될 시 user-agent를 정상적인 user-agent로 만들어서 접속하자
    <br/>

```python
import requests

headers ={
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

r = requests.get('https://www.amazon.com/ref=cs_503_logo',headers=headers)
print(r.content) # 아마존 봇에 막힘
print(r.status_code) # 200 잘됌

```

## 방법2:Cookies 첨부

> cookie정보를 header에 담아 같이 보내면됌

- f12-네트워크-Request Headers-맨첫번째꺼 클릭후-Request탭에서 `cookie`정보 복사

```python
import requests

headers ={
  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

cookie = {'ad-id': 'A9sVvHK15UUkjz8Vxh40zgQ', 'ad-privacy': '0'}

r = requests.get('https://www.amazon.com/ref=cs_503_logo',headers=headers,cookies=cookie)
print(r.content)
print(r.status_code)
```
