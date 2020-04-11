# -------------------------------------------------------- #
# -------------------------------------------------------- #
# ----이 프로그램의 api는 유료여서 가입 후 사용할 수 있습니다 ---- #
# -------------------------------------------------------- #
# -------------------------------------------------------- #
from urllib.error import HTTPError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
import random
import datetime

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html =urlopen('http://en.wikipedia.org{}'.format(articleUrl))
    bs =BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id':'bodyContent'}).findAll('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def getHistoryIPs(pageUrl):
    #계정 히스토리 페이지 형식은 다음과 같습니다.
    #http://en.wikipedia.org/w/index.php?title=Title_In_URL&amp;action=history
    pageUrl = pageUrl.replace('/wiki/', '')
    historyUrl = 'http://en.wikipedia.org/w/index.php?title='
    historyUrl += pageUrl + '&amp;action=history'
    print('history url is : {}'.format(historyUrl))
    html = urlopen(historyUrl)
    bs =BeautifulSoup(html, 'html.parser')
    #클래스가 "mw-anonuserlink"인, 사용자 이름이 아니라IP주소가 들어 있는 링크만 찾는다.

    ipAddresses = bs.findAll('a', {'class':'mw-anonuserlink'})
    addressList = set()

    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList

def getCountry(ipAddress):
    try:
        url = 'http://api.ipstack.com/' + ipAddress
        url += '?access_key=ACCESS_KEY&amp;format=1'
        response = urlopen(url).read().decode('utf-8')
    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get('country_code')


links = getLinks('/wiki/Python_(programming_language)')

while(len(links) > 0):
    for link in links:
        print('-'*20)
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            country = getCountry(historyIP)
            if country is not None:
                print('{} is from {}'.format(historyIP, country))

    newLink = links[random.randint(0, len(links)-1)].attrs['href']
    links = getLinks(newLink)