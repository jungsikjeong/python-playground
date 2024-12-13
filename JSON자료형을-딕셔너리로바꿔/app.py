## JSON을 딕셔너리로 바꾸기 예제


import requests
import json
import time

data = requests.get('https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h')
print(data.content)

딕셔너리 = json.loads(data.content) # ""로 감싸진 JSON데이터들이 ''로 감싸진 딕셔너리 형태로 변환됌

#epoch시간을 년월일시분초로 변환
for i in range(200):
  시간 = 딕셔너리['data'][i]['DT']
  글자시간 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(시간/1000)) 
  
  print(글자시간)
  print(딕셔너리['data'][i]['Close'])
