# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CarlingoItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    location = Field()
    price = Field()
    time=Field()
    type=Field()
    post = Field()
    notice = Field()
    # #have not include post id

    # # attr group
    # conditon=Field()
    # cylinders = Field()
    # drive = Field()
    # fuel = Field()
    # odometer = Field()
    # paint_color = Field()
    # size = Field()
    # title_status=Field()
    # transmission = Field()
    model = Field()
