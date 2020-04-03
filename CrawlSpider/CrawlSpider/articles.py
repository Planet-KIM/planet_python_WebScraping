from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class ArticleSpider(CrawlSpider):
    name = 'articles'
    allowed_domains = ['wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/'
    'Benevolent_dictator_for_life']
    rules = [Rule(LinkExtractor(allow=r'.*'), callback='parse_items', follow=True)]

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()
        text = response.xpath('//div[@id="mw-content-text"]//text()').extract()
        lastUpdated = response.css('li#footer-info-lastmod::text').extract_first()
        lastUpdated = lastUpdated.replace('This page was last edited on ','')

        print('URL is {}'.format(url))
        print('Title is {}'.format(title))
        print('Text is {}'.format(text))
        print('Last updated : {}'.format(lastUpdated))

    def parse_items(self, response):
        url = response.url
        title = response.css('h1::text').extract_first()

        text_rules = '//div[@id ="mw-content-text"]//text()'
        text = response.xpath(text_rules).extract()

        update_rule = 'li#footer-info-lastmod::text'
        update_delete = 'This page was last edited on '
        lastUpdated = response.css(update_rule).extract_first()
        lastUpdated = lastUpdated.replace(update_delete, '')

        print('URL is : {}'.format(url))
