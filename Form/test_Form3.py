import requests

session = requests.Session() #쿠키, 헤더, HTTPAdapters 같은 http에서 동작하는 프로토콜에 관한정보까지 관리.

params = {'username':'username', 'password':'password'}
welcome_page = 'http://pythonscraping.com/pages/cookies/welcome.php'
s = session.post(welcome_page, params)

print('Cookie is set to : ')
print(s.cookies.get_dict())
print('Going to profile page...')

profile_page = 'http://pythonscraping.com/pages/cookies/profile.php'
s = session.get(profile_page)
print(s.text)