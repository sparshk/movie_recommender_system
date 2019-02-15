import scrapy
from imdbscraper.items import MovieItem
 
class ImdbSpider(scrapy.Spider):
    name = "imdbspider"
    def start_requests(self):
        f = open('links.csv','r').readlines()
        for url in f:
            url='https://www.imdb.com/title/tt0'+url.strip()
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self,response):
        item = MovieItem()
        item['movie_id']=response.url[30:][:-1]
        item['imdb_url'] = response.url
        item['title'] = response.css('h1::text').extract_first().strip()
        item['year'] = response.css('#titleYear a::text').extract_first()
        item['users_rating'] = response.xpath(
            '//span[contains(@itemprop, "ratingValue")]/text()').extract_first()
        item['img_url'] = response.xpath(
            '//div[contains(@class, "poster")]/a/img/@src').extract_first()
        item['description'] = response.xpath(
            '//div[contains(@class, "summary_text")]/text()').extract_first().strip()
        genres = response.xpath(
            "//div[contains(.//h4, 'Genres')]/a/text()").extract()
        item['genre'] = [genre.strip() for genre in genres]
        return item
    