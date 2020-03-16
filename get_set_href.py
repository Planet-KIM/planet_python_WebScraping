#재귀적 방법으로 link 호출하여 실행하기.
#또한 중복링크는 set배열에 두고 중복처리.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

#set은 리스트와 비슷한 데이터 형식이지만....
#요소의 순서가 없고 중복이 없습니다.
pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    bs = BeautifulSoup(html, 'html.parser')
    
    for link in bs.findAll('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #new page 발견
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
                
getLinks('') 