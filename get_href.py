#위키백과 page를 가져와 page에 들어있는 링크 목록을 가져오는 스크립트
#수정할 사항 : 예외 처리를 해주어야 완벽합니다.
from urllib.request import urlopen
from bs4 import BeautifulSoup

import datetime
import random

import re #정규식을 표현하기 위한 라이브러리입니다.

#현재 시스템 시간으로 난수를 발생하여..
#실행할 때마다 무작위 경로를 얻어냄
random.seed(datetime.datetime.now()) #Mersenne Twister algorithm 파이썬의 의사 난수 발생기. 

#방법 3
#/wiki/<article_name> 형태인 위키백과 항목URL을 얻어내고, 링크된 항목 URL 목록전체를 반환하는 getLink Function
#시작 항목에서 getLinks를 호출하고 반환된 리스트에서 무작위로 항목링크를 선택하여 getLinks를 다시 호출.
#프로그램을 끝내거나 새 페이지에 항목 링크가 없을 때까지 무한한복합니다.  
def getLinks(articleUrl):
    html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    
    return bs.find('div', {'id' : 'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$'))    

links = getLinks('/wiki/Kevin_Bacon')

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

#방법 1
#for link in bs.findAll('a'):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

#방법 2
#방법 1의 link들은 id가 bodyContent인 div안에 있습니다.
#URL에는 콜론이 포함되어 있지 않습니다.
#URL에는 /wiki/로 시작됩니다.
#for link in bs.find('div', {'id' : 'bodyContent'}).findAll('a', href = re.compile('^(/wiki/)((?!:).)*$')):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])
    