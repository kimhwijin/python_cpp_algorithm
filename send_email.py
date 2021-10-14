import smtplib
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

class cEMail():
    # eMail Provide    SMTP ServerName    Port   추가 설정
    # Live             smtp.live.com      587
    # GMail            smtp.gmail.com     587    개인 설정->계정 액세스 권한을 가진 앱 ->보안 수준이 낮은 앱 허용: 사용
    def __init__(self,smtpServer, password):
        #print( "cEMail __init__")
        self.smtpServer=smtpServer
        self.smtp = smtplib.SMTP('smtp.gmail.com')
        self.smtp.ehlo()      # say Hello
        self.smtp.starttls()  # TLS 사용시 필요
        self.smtp.login(self.smtpServer, password)
    def __del__(self):
        #print( "cEMail __del__")
        try:self.smtp.quit()
        except:pass
    def send(self,toEMail,subject,message):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['Date'] = formatdate(localtime=True)
        msg['From'] = self.smtpServer
        msg['To'] = toEMail
        fromEMail=self.smtpServer
        self.smtp.sendmail(fromEMail, toEMail, msg.as_string())
    def sendAttached(self,toEMail,subject,message,files=[]):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['Date'] = formatdate(localtime=True)
        msg['From'] = self.smtpServer
        msg['To'] = toEMail
        msg.attach(MIMEText(message))
        for path in files:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
            email.encoders.encode_base64(part)
            part.add_header('Content-Disposition',
                            'attachment; filename="{}"'.format(os.path.basename(path)))
            msg.attach(part)
                  
        fromEMail=self.smtpServer
        self.smtp.sendmail(fromEMail, toEMail, msg.as_string())
        print("Complete to send EMail to destination...")
       

if __name__ == '__main__':

    smtp_server='rlagnlwls0160@gmail.com'
    smtp_server_password='gpajdexkafisrmqb'
    m_eMail =cEMail(smtp_server,smtp_server_password)
   
    toMail='rlagnlwls0160@gmail.com'
    Subject='Test Mail'
    Message='안녕하세요 \n이 메일은  파이썬에서 보내는 테스트 메일 입니다.\n감사합니다.'
    m_eMail.send(toMail,Subject,Message)


   