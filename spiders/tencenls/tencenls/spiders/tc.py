# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from tencenls.items import TencenlsItem


# class TcSpider(CrawlSpider):
class TcSpider(RedisCrawlSpider):
    # name = 'tc'
    # allowed_domains = ['tencent.com']
    # start_urls = ['http://hr.tencent.com/position.php?&start=0#a']
    # #Response里链接的提取规则，返回的符合匹配的链接匹配对象的列表
    # papgelink = LinkExtractor(allow=("start=\d+"))
    #
    # rules = (
    #     #获取这个列表的链接，依次发送请求，并且继续跟进，调用指定的回调函数进行处理
    #     Rule(papgelink, callback='parseContent', follow=True),
    # )
    # # #指定的回调函数


    name = 'tc'
    redis_key = "tcspider:start_urls"

    # 动态域范围获取
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(TcSpider, self).__init__(*args, **kwargs)





    papgelink = LinkExtractor(allow=(r"start=\d+"))

    rules = (
        #获取这个列表的链接，依次发送请求，并且继续跟进，调用指定的回调函数进行处理
        Rule(papgelink, callback='parseContent', follow=True),
    )
    #指定的回调函数




    def parseContent(self, response):

        for each in response.xpath("/tr[@class='even'] | //tr[@class='odd']"):
            name = each.xpath('./td[1]/a/text()').extract()[0]
            detailLink = each.xpath('./td[1]/a/@href').extract()[0]
            positionInfo = each.xpath('./td[2]/text()').extract()[0]

            peopleNumber = each.xpath('./td[3]/text()').extract()[0]
            workLocation = each.xpath('./td[4]/text()').extract()[0]
            publishTime = each.xpath('./td[5]/text()').extract()[0]
            #print name, detailLink, catalog,recruitNumber,workLocation,publishTime

            item = TencenlsItem()
            #职位名称
            item['positionname']=name
            #详细链接
            item['positionlink']=detailLink
            #职位详情
            item['positionType']=positionInfo
            #招聘人数
            item['pepopleNum']=peopleNumber
            #工作地点
            item['workLocation']=workLocation
            #发布时间
            item['pulishTime']=publishTime

            yield item
