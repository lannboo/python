# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    positionname = scrapy.Field()

    #link
    positionlink = scrapy.Field()

    #tpye
    positionType = scrapy.Field()

    #
    pepopleNum = scrapy.Field()

    #
    workLocation = scrapy.Field()

    #pulishTime
    pulishTime = scrapy.Field()

    
    
