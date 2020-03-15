from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 범용 함수화 #
#-------Return Title def-------#
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None

    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        print(e)
        return None

    return title
#-----------------------------#
title = getTitle('http://pythonscraping.com/pages/page1.html')

if title == None:
    print('Title could not be found')
else:
    print(title)
