import sys
from bs4 import BeautifulSoup

import io
from urllib.request import urlopen


def chageUtf8():
    sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

chageUtf8()

html = 'http://www.pythonscraping.com/pages/page3.html'
bs = BeautifulSoup(html, 'html.parser')

print(bs.get_text())