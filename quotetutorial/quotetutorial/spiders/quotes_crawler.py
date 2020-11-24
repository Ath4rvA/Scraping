import scrapy
from ..items import QuotetutorialItem

class QuoteSpider(scrapy.Spider):

    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def __init__(self):
        self.items = QuotetutorialItem()

    def parse(self, response):

        # title = response.css('title::text').extract()

        divs = response.css('div.quote')
        for div in divs:
            self.items['quote'] = div.css('span.text::text').extract()[0]
            self.items['author'] = div.css('.author::text').extract()[0]
            self.items['tags'] = div.css('a.tag::text').extract()
            yield self.items
