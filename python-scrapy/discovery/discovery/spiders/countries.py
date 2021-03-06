import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['http://www.worldometers.info/world-population/population-by-country']

    def parse(self, response):
        countries = response.xpath("//td/a").getall()
        for country in countries:
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

        yield response.follow(url=link)
