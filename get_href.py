#위키백과 page를 가져와 page에 들어있는 링크 목록을 가져오는 스크립트
from urllib.request import urlopen
from bs4 import BeautifulSoup

import re #정규식을 표현하기 위한 라이브러리입니다.

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

#방법 1
#for link in bs.findAll('a'):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

#방법 2
#방법 1의 link들은 id가 bodyContent인 div안에 있습니다.
#URL에는 콜론이 포함되어 있지 않습니다.
#URL에는 /wiki/로 시작됩니다.
for link in bs.find('div', {'id' : 'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
    