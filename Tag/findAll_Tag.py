from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

#nameList = bs.findAll('span', {'class' : 'red'}) #단일 Tag
#nameList = bs.findAll('span', {'class':{'green', 'red'}}) #어러개의 Tag

#nameList = bs.findAll(text = 'the prince') #text의 해당 항목이 포함되어있으면 출력.

nameList = bs.findAll('', {'class' :{'red', 'green'}}) #이 방식은 밑의 방식을 대체할 수 있으나 여러개의 값을 받을 수 있음.
nameList = bs.findAll(class_ = 'red') #이러한 형식은 위를 대체할 수는 있으나 단일만 됨.

for name in nameList:
    print(name.get_text())
print(len(nameList))
