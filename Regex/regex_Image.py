from urllib.request import urlopen as uo
from bs4 import BeautifulSoup 

import re

html = uo('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

images = bs.findAll('img', {'src' : re.compile('\.\.\/img\/gifts/img.*\.jpg')})

print(bs.attrs['src'])

for image in images:
    print(image['src'])