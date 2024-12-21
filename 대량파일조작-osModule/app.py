import os #파이썬으로 파일 조작할 때 많이 쓰임

# 이 경로에 있는 파일명들 다 가져오기
files= os.listdir('test')
print(files)

# test/1.txt-> 4.txt파일명으로 변경됌
os.rename('test/1.txt','test/4.txt')

# test폴더안에있는 모든 파일들을 반복분으로 돌면서 이름을 변경
for i in os.listdir('test'):
  os.rename(f'test/{i}',f'test/good{i}')



# 파일을 복사하는 방법
import shutil

shutil.copy('/4.txt','test/5.txt') #4.txt를 5.txt로 복사

#test폴더에 있는 파일들을 test2폴더로 복사
for i in os.listdir('test'):
  shutil.copy(f'test/{i}',f'test2/{i}') 

for i in os.listdir('test'):
  if 만약에지금i라는파일명에 jpg가 들어있으면:
    shutil.copy(f'test/{i}',f'test2/{i}') #test폴더에 있는 파일들을 test2폴더로 복사



