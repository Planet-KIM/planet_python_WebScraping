'''
1. 이론적으로는 GIL은 프로세스를 잠그지 않으므로 여러프로세스가 동시에 같은
코드를 실행할 수 있고 동시에 같은 객체(같은 객체의 서로 다른 인스턴스)에
접근할 수 있습니다.
2. 프로세스는 멀티코어를 활용할 수 있으므로, 프로세스나 스레드가 cpu에 의존적
이라면 성능이 더 올라갈 수 있습니다.
3. 프로세스는 각각 독립적인 메모리 공간 안에서 동작하므로 별도의 조치 없이
서로 정보를 공유할 수 없습니다. (큐와 파이프를 사용하여 개선)
'''
'''
단점 : url은 모두 전역 visited 리스트에 저장(모든 스레드가 공유)
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

from multiprocessing import Process
import os
import time

visited = []

def get_links(bs):
    print('Getting links in {}'.format(os.getpid()))
    links = bs.find('div',{'id':'bodyContent'}).find_all('a',
                                                         href=re.compile('^(/wiki/)((?!:).)*$'))
    return [link for link in links if link not in visited]

def scrape_article(path):
    visited.append(path)
    print("Process {} list is now: {}".format(os.getpid(), visited))
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    time.sleep(5)
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1').get_text()
    print('Scraping {} in process {}'.format(title, os.getpid()))
    links = get_links(bs)
    if len(links) > 0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        scrape_article(newArticle)

if __name__ == '__main__':
    processes = []
    processes.append(Process(target=scrape_article, args=('/wiki/Kevin_Bacon',)))
    processes.append(Process(target=scrape_article, args=('/wiki/Monty_Python',)))

    for p in processes:
        p.start()

