from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page2.html')

bs = BeautifulSoup(html, 'html.parser')

#lts = bs.findAll(lambda tag: len(tag.attrs) == 2) #Tag 속성이 두개인 것을 출력

#Tag에 해당 텍스트가 있으면.. 출력합니다
#해당 텍스트가 전부 있어야 가져옵니다.
#lts = bs.findAll(lambda tag: tag.get_text() == 'An Interesting Title')

#위와 같은 방법이나 Tag까지 출력하지 않고 깔끔하게 text만 출력합니다. 
lts = bs.findAll('', text='An Interesting Title')

for lt in lts:
    print(lt)