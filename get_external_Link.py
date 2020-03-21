#예외 처리가 필요한 라이브러리입니다.
#외부 링크를 찾을 때까지 웹사이트를 재귀적으로 찾는 방법입니다.
from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

import os

pages = set()
random.seed(datetime.datetime.now())

#페이지에서 발견된 내부링크를 모두 목록으로 만드는 function
def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    # /로 시작하는 링크를 모두 찾습니다.
    for link in bs.findAll('a', href = re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if(link.attrs['href'].startswith('/')):
                internalLinks.append(includeUrl + link.attrs['href'])
            else:
                internalLinks.append(link.attrs['href'])
    return internalLinks
    
#페이지에서 발견된 외부링크를 모두 목록으로 만드는 function
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #현재 URL을 포함하지 않으면서 http나 www로 시작하는 링크를 모두찾습니다.
    for link in bs.findAll('a', href = re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
    
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bs = BeautifulSoup(html, 'html.parser')
    
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
        
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)
    
followExternalOnly('http://oreilly.com')
