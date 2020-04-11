import requests

'''
params ={'firstname':'Ryan', 'lastname':'Mitchell'}
r = requests.post('http://pythonscraping.com/pages/processing.php', data=params)
print(r.text) #폼을 전송하면 페이지 콘텐츠가 반환됩니다.
'''
'''
params ={'email_addr':'your_email@gmail.com'}
url = 'http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi'
r = requests.post(url, data=params)
print(r.text)
'''

#상대경로에 있는 이미지를 폼을 이용하여 전송하는 것.
files = {'uploadFile':open('files/Python-logo.png', 'rb')}
url ='http://pythonscraping.com/pages/processing2.php'
r = requests.post(url, files=files)
print(r.text)