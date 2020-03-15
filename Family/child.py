from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#table id가 giftList인 태그에 자식들을 전부 출력해주는 구문. 태그 조차 출력해줍니다.
#for child in bs.find('table', {'id' : 'giftList'}).children:
#    print(child)


#형제 다루기 
#Table에서 타이틀 행이 있을 때 데이터를 쉽게 수집할 수 있는 구문.    
for sibling in bs.find('table', {'id' : 'giftList'}).tr.next_siblings:
    print(sibling)