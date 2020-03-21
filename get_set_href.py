#재귀적 방법으로 link 호출하여 실행하기.
#또한 중복링크는 set배열에 두고 중복처리.
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

import os

#folder를 체크해주고 생성해주는 function 라이브러리입니다.
#이를 조금 더 개선하여서 폴더의 존재여부를 체크해줘야합니다.
def crateFolder(folder):
    try:
        if not os.path.exists(folder):
            os.mkdir(folder)
    except OSError as e:
        print('Foleder is exists' + folder)

#path를 사용자에게 입력받고 이를 crateFolder function에 인수로 줍니다.
path = './data'
crateFolder(path)

#크롤링한 데이터를 파일로 저장하기 위해서 조치한 수단.
filepath = os.path.join(path, 'scraping_data')
file = open(filepath, 'w')

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
                #폴더에 파일존재 여부 파악하고 데이터 삽입하기....
                if not os.path.isfile(filepath):
                    print('file content input success!!!')
                    file.write(str(newPage) +'\n')

                pages.add(newPage)
                getLinks(newPage)

getLinks('')
print('file uploading success!!\n')
file.close()
print('complete program')
