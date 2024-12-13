# 현재 시간 출력
import time

print(time.time()) # 1611304823.0758648 이런식으로 현재 Epoch 출려됌


# 현재 ctime 출력 방법
시간= time.time()
시간 = time.ctime(시간) # Thu Jan 21 22:42:49 2021 

시간 = time.localtime() # localtime()으로 세부항목만 출력하기
print(시간.tm_year) # 2024

#time.strftime('포맷팅문법',시간) - 사용법
a = time.strftime("%Y year-%m month",시간)
print(a)


# 훨씬 더 간단히 시간 출력방법
import datetime
datetime.datetime(2024,12,14)