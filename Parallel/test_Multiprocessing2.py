from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random
from multiprocessing import Process, Queue
import os
import time

def task_delegator(taskQueue, urlsQueue):
    #각 프로세스에서 처리할 작업을 초기화합니다.
    visited = ['/wiki/Kevin_Bacon', '/wiki/Monty_Python']
    taskQueue.put('/wiki/Kevin_Bacon')
    taskQueue.put('/wiki/Monty_Python')

    while 1:
        #urlsQueue에 처리할 새 링크가 있는지 확인합니다.
        if not urlsQueue.empty():
            links = [link for link in urlsQueue.get() if link not in visited]
            for link in links:
                #새 링크를 taskQueue에 추가합니다.
                taskQueue.put(link)

def get_links(bs):
    links = bs.find('div',{'id':'bodyContent'}).find_all('a',
                                                         href=re.compile('^(/wiki/)((?!:).)*$'))
    return [link.attrs['href'] for link in links]

def scrape_article(taskQueue, urlsQueue):
    while 1:
        while taskQueue.empty():
            #작업 큐가 비어 있으면 0.1초 대기합니다. 이런일은 드물게 일어납니다.
            time.sleep(.1)
        path = taskQueue.get()
        html = urlopen('http://en.wikipedia.org{}'.format(path))
        bs = BeautifulSoup(html, 'html.parser')
        title = bs.find('h1').get_text()
        print('Scraping {} in process {}'.format(title, os.getpid()))
        links = get_links(bs)
        #찾아낸 링크를 위임자에 보내 처리하게 됩니다.
        urlsQueue.put(links)

if __name__ == '__main__':
    processes = []
    taskQueue = Queue()
    urlsQueue = Queue()

    processes.append(Process(target=task_delegator, args=(taskQueue, urlsQueue,)))
    processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue,)))
    processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue,)))

    for p in processes:
        p.start()