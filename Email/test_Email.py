import smtplib
from email.mime.text import MIMEText

msg = MIMEText('hello text message')

msg['Submit'] = 'An Email Alert'
msg['From'] = 'ryan@pythonscraping.com'
msg['To'] = 'kdw59520@gmail.com'

s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()