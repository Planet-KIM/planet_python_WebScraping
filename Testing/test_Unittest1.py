from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest

class TestWikiepda(unittest.TestCase):
    bs = None
    #setUp과는 달리 클래스를 시작할 때 한번만 실행합니다.
    #불필요한 로딩을 줄이고 페이지 콘텐츠를 한 번만 불러와서 여러 테스트를 실행할 수 있습니다.
    def setUpClass():
        url = 'http://en.wikipedia.org/wiki/Monty_Python'
        TestWikiepda.bs = BeautifulSoup(urlopen(url), 'html.parser')

    def test_titleText(self):
        pageTitle = TestWikiepda.bs.find('h1').get_text()
        self.assertEqual('Monty Python', pageTitle);

    def test_contentExists(self):
        content = TestWikiepda.bs.find('div', {'id':'mw-content-text'})
        self.assertIsNotNone(content)

if __name__ == '__main__':
    unittest.main()