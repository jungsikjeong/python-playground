# # pip install Pillow

from PIL import Image

img= Image.open('images/photo1.jpg')
img.thumbnail((300,500)) # 비율 유지하며서 리사이즈
 # jpg는 quality=로 저장할때 압축가능함 숫자가 높을수록 고화질로 저장됨 0~95고, 기본값은 75로 자동설정되어있음
 # png라면 quantize 옵션을 찾아보자
img.save('new_photo1.jpg',quality=65)


# img= img.resize((300,500)) # 비율 깨지면서 리사이즈


# 만약 png파일을 jpg로 변환하고싶으면 간단하게 png파일 open후, jpg로 저장하자
img= Image.open('images/photo1.png')
img.thumbnail((300,500)) 
img.save('new_photo1.jpg',quality=65)


# 혹은 Progressive JPG로 만들기 가능
img.save('new_photo1.jpg',Progressive=True)

# 이미지 옵션 몇가지 더..
# 이미지를 잘라줌, 좌표로 동작함
img = img.crop((50,50,150,150))

# 흑백변환
img = Image.open('images/photo1.jpg').convert('L')

# images폴더내의 많은 이미지를 한번에 리사이즈?
from PIL import Image
import os 

경로 = os.getcwd() # 절대경로
파일명들 = os.listdir(경로 + '/images')
img= Image.open('images/photo1.jpg')

for 파일명 in 파일명들:
  img = Image.open('images/' + 파일명)
  img.thumbnail((500,2500))
  img = img.save('new_' + 파일명)
