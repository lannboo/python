# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#import scrapy

from scrapy import Field,Item


class TencenlsItem(Item):
    # define the fields for your item here like:
    positionname = Field()

    #link
    positionlink = Field()

    #tpye
    positionType = Field()

    #
    pepopleNum = Field()

    #
    workLocation = Field()

    #pulishTime
    pulishTime = Field()
