# 크롤러 만들었는데 시간이 오래걸릴경우 완료를 알려주거나 
# 결과 파일을 전송해주거나 그럴 때 이메일 사용함

import smtplib
from email.mime.text import MIMEText
 

from email.mime.multipart import MIMEMultipart
 
 # """ 엔터키 자유롭게 칠 수 있는 문자 따옴표 세개 """

msg = MIMEMultipart('alternative') #HTML전송할 때 필요한 함수
내용 = """
여기에 HTML로 작성가능
"""
part1 = MIMEText(내용, "html")
msg.attach(part1)

 
msg['Subject'] ="이것은 메일제목"
msg['From'] = 'wndtlr1024@naver.com'
msg['To'] = '김대리'#받는사람이름이나 이메일
print(msg.as_string())
 
# s = smtplib.SMTP( '네이버smtp주소' , 포트번호 ) 
s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 

s.starttls() #TLS 보안 처리
s.login( 'wndtlr1024' , 'SMTP비번' ) #네이버로그인, 비밀번호에는 따로 smtp 비밀번호설정해준것을 적어주면됌
s.sendmail( 'wndtlr1024@naver.com', 'wndtlr1024@gmail.com', msg.as_string() )
s.close()




# 아래처럼하면 첨부파일도 넣을 수 있음
import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

text = "메일 내용입니다"
msg = MIMEMultipart()
msg['Subject'] ="이것은 메일제목"
msg['From'] = '보내는자이메일'
msg['To'] = '받는자이메일또는이름'
msg.attach(MIMEText(text))
print(msg.as_string())

#원하는 파일 rb로 오픈
with open('보낼파일경로', 'rb') as 파일:
  part = MIMEBase('application', 'octet-stream')
  part.set_payload(파일.read())

#파일 base64 인코딩
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="경로제외보낼파일명"')
msg.attach(part)

s = smtplib.SMTP( 'smtp.naver.com' , 587 ) 
s.starttls()
s.login( '네이버아이디' , '비번' ) 
s.sendmail( '보내는사람', '받는사람', msg.as_string() ) 
s.close()