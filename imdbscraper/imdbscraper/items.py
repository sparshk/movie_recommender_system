# -*- coding: utf-8 -*-

# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class MovieItem(scrapy.Item):
    
#defining our item fields
    movie_id=scrapy.Field()
    imdb_url=scrapy.Field()
    title = scrapy.Field()
    year=scrapy.Field()
    users_rating = scrapy.Field()
    img_url=scrapy.Field()
    description=scrapy.Field()
    genre=scrapy.Field()