import scrapy


class LancaHorasSpider(scrapy.Spider):
    name = 'lanca_horas'
    allowed_domains = ['discovery.leega.com.br']
    start_urls = ['http://discovery.leega.com.br/']

    def parse(self, response):
        username = response.xpath('//*[@id="Login"]').get()
        password = response.xpath('//*[@id="Password"]').get()
        
        yield {
            'username'
        }
