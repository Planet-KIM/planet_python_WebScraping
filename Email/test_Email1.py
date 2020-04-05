from urllib.request import urlopen
from bs4 import BeautifulSoup

import time
import smtplib
from email.mime.text import MIMEText

def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'kdw59520@gmail.com'
    msg['To'] = 'kdw59520@gmail.com'
    
    s = smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()
    
bs = BeautifulSoup(urlopen("https://isitchristmas.com/"))
while(bs.find("a", {"id":"answer"}).attrs['title'] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
    bs = BeautifulSoup(urlopen("https://isitchristmas.com/"))
    
sendMail("It's Christmas!", "According to http://itischristmas.com, it is Christmas!")
