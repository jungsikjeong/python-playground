import requests
import json
import time


# 수집하고싶은 url이 매우 많을경우에 for 돌리면 순차적으로 한줄한줄 실행도어 시간이 오래걸릴 수 있음
# (천개, 만개 등등..)
url = [
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1609524000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608811200000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1608098400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1606672800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605960000000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1605242700000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1604534400000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603821600000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1603108800000',
  'https://tb.coinone.co.kr/api/v1/chart/olhc/?site=coinoneeth&type=1h&last_time=1602396000000'
]

def 함수(구멍):
  data =requests.get(구멍)
  딕셔너리=json.loads(data.content)
  return 딕셔너리['data'][0]['Close']

함수(url[0])

# 멀티 프로세싱
# 주의점: process가 여러개있으면 한 process가 변수를 수정할때 그 변수는 lock이걸림
# 다른 process가 또 그 변수를 수정하려고하려면 앞전 process가 그 변수를 다 수정할 때 까지 기다리게됌
# 이렇게 병목현산이 발생하기때문에 테스트나, 주의해서 코드를 사용해야함

# from multiprocessing import Pool as ThreadPool 이렇게해도 Pool함수 그대로 쓸 순있음
# multiprocessing.dummy까지붙이면 멀티쓰레딩으로 코드 실행가능
from multiprocessing.dummy import Pool as ThreadPool

pool = ThreadPool(4) #몇개 쓰레딩을 활성화할건지
pool.map(작업시킬함수,작업시킬리스트) 
pool.close() # 종료
pool.join() # 결과 나올때까지 기다려달라는것
