from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

#해당 src에 해당하는 이미지를 찾습니다.
#부모 tag를 선택합니다.
#부모 tag에 았는 text를 출력합니다.
print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())
