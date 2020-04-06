import smtplib
from email.mime.text import MIMEText

smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login('kdw59520@gmail.com', 'password')

msg = MIMEText('hello text message')
msg['Submit'] = 'An Email Alert'
msg['From'] = 'ryan@pythonscraping.com'
msg['To'] = 'kdw59520@gmail.com'


smtp.sendmail('kdw59520gmail.com', 'kdw59520gmail.com', msg.as_string())
smtp.quit()