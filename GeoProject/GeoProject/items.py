# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IgepnItem(scrapy.Item):
    # define the fields for your item here like:
    Latitud = scrapy.Field()
    Longitud = scrapy.Field()
    Profundidad = scrapy.Field()
    Fecha = scrapy.Field()
    Z = scrapy.Field()

