# JSON 형식을 파이썬 딕셔너리로 바꾸기

## JSON, 딕셔너리

- JSON 형식은 키, 값의 형식으로 되어있으며 큰 따옴표만 사용하는 형식

- 딕셔너리는 python의 자료구조이며, 자바스크립트의 객체와 유사하다.
  key값으로 숫자나,튜플타입이 사용 가능하다.

## JSON을 딕셔너리로 바꾸기 예제

```python
import requests
import josn

data = requests.get('url')
print(data.content)

딕셔너리 = json.loads(data.content) # ""로 감싸진 JSON데이터들이 ''로 감싸진 딕셔너리 형태로 변환됌
print(딕셔너리)

```
