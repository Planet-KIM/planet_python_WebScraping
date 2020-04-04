from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article

class ArticleSpider(CrawlSpider):
    name  = 'articlePipelines'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://wikipedia.org/wiki/Benevolent''_dictator_for_life']
    rules = [
        Rule(LinkExtractor(allow='en.wikipedia.org/wiki/((?!:).)*$'),
        callback='parse_items', follow=True),
    ]

    def parse_items(self, response):
        article = Article()
        article['url'] = response.url
        article['title'] = response.css('h1::text').extract_first()
        article['text'] = response.xpath('//div[@id=''"mw-content-text"]//text()').extract()
        article['lastUpdated'] = response.css('li#''footer-info-lastmod::text').extract_first()
        #article['lastUpdated'] = lastUpdated.replace('This page was ''last edited on', '')
        return article

    '''
    def start_requests(self):
        urls = [
            'http://en.wikipedia.org/wiki/Python_'
            '%28programming_language%29',
            'https://en.wikipedia.org/wiki/Functional_programming',
            'https://en.wikipedia.org/wiki/Monty_Python'
        ]
        return [scrapy.Request(url=url, callback=self.parse) for url in urls]

    def parse(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        print('Url is {}'.format(url))
        print('Title is {}'.format(title))
    '''
