import requests
from bs4 import BeautifulSoup


def changeUtf8():
    import sys
    import io

    #파일을 utf-8로 인코딩하기 위해 사용하는 구문
    #atom에 자동적으로 파일을 utf-8로 인코딩 한다고 하나 오류가 걸리는 경우가 많아서 사용
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


changeUtf8()

class Content:
    def __init__(self,topic, url, title, body):
        self.topic = topic
        self.url = url
        self.title = title
        self.body = body

    def prints(self):
        print('New article found for topic : {}'.format(self.topic))
        print("URL : {}".format(self.url))
        print("TITLE : {}".format(self.title))
        print("BODY :\n{}".format(self.body))

class Website:
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Clawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')

    def safeGet(self, pageObj, selector):

        #BeautifulSoup 객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수 주어진 선택자로 검색된
        #결과가 없다면 빈 문자열을 반환합니다.

        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ''

    def search(self, topic, site):
        #주어진 검색어로 주어진 웹사이트를 검색해 결과 페이지를 모두 기록합니다.

        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing) #Why have a error?

        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs['href']
            #상대 url인지 절대 url인지 확인합니다.
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print('Something was wrong with that page or URL =,Skipping!')
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.prints()

"""
    def parse(self, site, url):
        #url을 받아 콘턴츠를 추출합니다.
        bs = self.getPage(url)

        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.prints()
"""

crawler = Clawler()

"""
siteData = [
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'],
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://brookings.edu', 'h1', 'div.post-body']
]

websites = []
urls =[
    'http://shop.oreilly.com/product/063920028154.do',
    'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0',
    'http://www.brookings.edu/blog/techtank/2016/03/01//idea-to-retire-old-methods-of-policy-education/'
]
"""

siteData =[
    ['O\'Reilly Media',
        'http://oreilly.com',
        'https://ssearch.oreilly.com/?q=',
        'article.product-result',
        'p.title a',
        True,
        'h1',
        'section#product-description'],
    ['Reuters',
     'http://reuters.com',
     'http://www.reuters.com/search/news?blob=',
     'div.search-result-content',
     'h3.search-result-title a',
     False,
     'h1',
     'div.StandardArticleBody_body_1gnLA'],
    ['Brookings',
    'http://www.brookings.edu',
    'http://www.brooking.edu/search/?s',
    'div.list-content article',
    'h4.title a',
    True,
    'h1',
    'div.post-body']
]

sites = []

for row in siteData:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

"""
crawler.parse(websites[0], urls[0])
crawler.parse(websites[1], urls[1])
crawler.parse(websites[2], urls[2])
"""

topics = ['python', 'data science']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
