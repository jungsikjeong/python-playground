## 채팅 서비스

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(response.choices[0].message.content)
```

- "role": "system": GPT를 세뇌하는 부분임. 프롬프트로 설정할게 있으면 여기에 적자

- "role": "user"는 유저의 질문 넣는 곳

- "role": "assistant"는 모범답안 예시를 넣는 곳"<br/>

EX)"유저가 누가 2020년에 월드시리즈 우승했니?" 라고 물어봤을 때 <br/>
"assistant는 Los Angeles Dodgers가 우승했다"<br/>
이런 식으로 답변하라고 예시를 줌<br/>

참고로 모범 답안 예시를 주는것을 `few shot prompting` 라고함<br/>
결과가 원하는대로 잘 안나올 경우 쓰고, 평소엔 쓸 일 잘 없음<br/>
few shot prompting를 많이 쓰면 비용도 증가하게됌

### 예시

```python
from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "너는 지금부터 코딩애플이라는 사이트의 고객상담원이다. 사이트에는 Python, JavaScript, React, Next.js, Node.js, Spring Boot 강의가 있다."},
    {"role": "user", "content": "제가 백엔드를 공부하고 싶은데 어떤 강의를 들어야할까요?"}
  ]
)

print(response.choices[0].message.content)
```

## 아이콘 생성

> `Dall-e 3`모델 활용 <br/>

### 예제

- 고양이사진을 생성해서 어디 하드에 임시로 올려주고 URL을 보내준다.

- 브라우저에 URL 입력하면 이미지가 나온다.

- 단. 대충 적으면 AI 느낌이 잔뜩 나는 이미지만 뽑아주기 때문에 프롬프트를 잘 써야한다.

```python

from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

```

추가 예시로, 심플한 선만 들어있는 아이콘을 생성하고싶다면<br/>
`"line art"` 라는 키워드를 넣으면 됌
