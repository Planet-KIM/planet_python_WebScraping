from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
 
import sys
import io
import os

def changeUtf8():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


def createFolder(folderName):
    try:
        if not os.path.exists(folderName):
            os.mkdir(folderName)
        except OSError as e:
            print('Folder is exists :' + folderName)
    
#인코딩하기 위해 필요한 것 입니다.
changeUtf8()
"""
folderName = './data'
createFolder(folderName)
"""

pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen('http://en.wikipedia.org'+pageUrl)
    bs = BeautifulSoup(html, 'html.parser')

    try:
        print(bs.h1.get_text())
        print(bs.find(id = 'mw-content-text').findAll('p')[0])
        print(bs.find(id = 'ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! No worries though!')

    for link in bs.findAll('a', href = re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print('--------------------\n'+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks('')
