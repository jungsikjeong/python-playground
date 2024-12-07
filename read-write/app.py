# 연습해본내용임.


리스트 =  [ '삼성전자', '카카오', '네이버', '신풍제약' ] 

리스트 = open('a.txt','w')
리스트.write('삼성전자\n 카카오\n 신풍제약')
리스트.close()


for i in range(2,10):
  for j in range(1,10):
    print(f"{i} X {j} = {i*j}")