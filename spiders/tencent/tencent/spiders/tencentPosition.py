# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['tencent.com']

    offset = 0
    url  = "https://hr.tencent.com/position.php?&start="
    start_urls = [ url + str(offset)]

    def parse(self, response):
        
        for each in response.xpath("/tr[@class='even'] | //tr[@class='odd']"):
        	
        	item = TencentItem()

        	item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
        	item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
        	item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
        	item['pepopleNum'] = each.xpath("./td[3]/text()").extract()[0]
        	item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
        	item['pulishTime'] = each.xpath("./td[5]/text()").extract()[0]

        	yield item
		    
		    

		if self.offset < 3760:
			self.offset  += 10
		else:
		   	raise "game  over !!!"
		   	break

		yield scrapy.Request(self.url + str(self.offset),callback = self.parse)

		    
