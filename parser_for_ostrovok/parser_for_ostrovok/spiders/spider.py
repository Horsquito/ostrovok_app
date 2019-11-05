import scrapy
from ..items import ParserForOstrovokItem


class QuotesSpider(scrapy.Spider):
    name = "spider"


    def start_requests(self):
        month_hash = {'12': 'january', '01': 'february', '02': 'march',
                '03': 'april', '04': 'may','05': 'june', '06': 'july',
                '07': 'august', '08': 'september', '09': 'october',
                '10': 'november', '11': 'december'}
        year = self.year
        month = self.month
        if month == '12':
            url = f'https://www.smashingmagazine.com/{int(year)-1}/{month}/desktop-wallpaper-calendars-{month_hash[month]}-{year}/'
        else:
            url = f'https://www.smashingmagazine.com/{year}/{month}/desktop-wallpaper-calendars-{month_hash[month]}-{year}/'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        item = ParserForOstrovokItem()
        image_urls = []
        links = response.xpath('//div[@id="article__content"]/div[@class="c-garfield-the-cat"]/ul/li /a/@href').getall()
        for img in links:
            if self.resolution in img:
                image_urls.append(img)
        item['image_urls'] = image_urls
        yield item
