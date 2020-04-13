from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
import _thread
import time

######### 고민해 봐야할 문제 #########
# 경쟁 상태를 고민해봐야합니다.

visited = [] # 중복링크 제거를 위한 배열
def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    links = bs.find('div', {'id':'bodyContent'}).find_all('a',
                                                         href=re.compile('^(/wiki/)((?!:).)*$'))
    return [link for link in links if link not in visited] # 중복 링크를 없애기 위한 배열작업입니다.


# 스레드에서 실행할 함수입니다.
def scrape_article(thread_name, path):
    visited.append(path) # 링크(path)를 배열에 전부 추가합니다.
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    time.sleep(5)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    print('Scraping {} in thread {}'.format(title, thread_name))
    links = get_links(thread_name, bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        scrape_article(thread_name, newArticle)

# 스레드 두개를 만듭니다.
try:
    _thread.start_new_thread(scrape_article, ('Thread 1', '/wiki/Kevin_Bacon',))
    _thread.start_new_thread(scrape_article, ('Thread 2', '/wiki/Monty_Python',))
except:
    print('Error : unable to start threads')

while 1:
    pass