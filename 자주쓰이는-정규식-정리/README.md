# 정규식

- 전처리가 가능하다.
  - 데이터 사이에 문자,날짜형식 다르고, 중복된 데이터 및 오타등등을 쉽게 전처리가 가능하다.

<br/>

사용은 이렇게 한다.

```python
import re

re.search('정규식','안녕하세요정규식')
```

`re.search('이글자가','여기있나요')`<br/>
있으면 object자료를 뱉어주고,<br/>
없으면 `None`를 뱉어준다.<br/>

```python
import re

a= re.findall('정규식','안녕하세요정규식')
print(a) # ['a']

```

`findall`은 [list] 자료형에 담아서 이쁘게 보여준다.<br>
이 밖에도 다양한 정규식표현이있다.

```python
b= re.findall('^a','abcde') # 이글자가 a로 시작하냐?

c = re.findall('c$','abcdef') # 이글자 끝이 c로 끝나냐?

d = re.findall('\$','asadsad$f^g') # 특수문자 찾으려면 \특수문자

e = re.findall('[abc]','asadsad$f^g') # 이거 or 저거 찾아주세요, a또는 b또는 c를 만족하는것을 다 찾아준다. print ['a','b','c']

e = re.findall('[a-zA-z]','asadsad$f^g') # 소문자 대문자 들어가있는지 검사 가능

e = re.findall('[가-힣ㄱ-ㅎ]','asadsad$f^g') # 한글 문자 들어오는지 검사 가능

e = re.findall('[^0-9]','aabsdfd') # ^ 쓰면 'not', []안에서 ^를쓰면 0부터9가 아닌것들을 찾는거임
```

좀 더 다양한것은 다음과 같다.

```python
a = re.findall('\d','as33') # 모든 숫자를 검사

a = re.findall('\D','as33') # 숫자가 아닌것을 검사

a = re.findall('\s','as 33') # 스페이스바 검사

a = re.findall('\S','as 33') # 스페이스바가 아닌 모든것을 검사 (모든 문자)

a = re.findall('a+','aaaaa') # 반복된 문자 찾는거 a가 반복되는것들 가져옴

a = re.findall('abc','Abcdaaaa',re.IGNOREACSE) # abc 대소문자 가리지않고 다 찾아줌 print: ['Abc']

```

이 외에도 기존 문자를 다른 문자로 바꾸기도 가능하다.<br/>
기본 사용법은 이렇다.<br/>

`re.sub('이걸찾아서','이걸로바꿔주세요','문장')` <br/>
좀더 자세히는 다음과 같다.

```python
import re

re.sub('\-','.','2022-1-1') # 2022.1.1
```
