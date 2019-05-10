# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dongguan.items import DongguanItem


class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://d.wz.sun0769.com/index.php/question/questionType?type=4&page=']

    #每一页匹配规则
    pagelink = LinkExtractor(allow=(r"type=4&page=\d+"))

    #每一页里的每一个帖子的链接匹配规则
    contentlink = LinkExtractor(allow=(r'/html/question/\d+/\d+.shtml'))

    rules = (
        #本案例的url被服务器篡改,需要调用process_links 来处理提取出来的url
        Rule(pagelink,process_links= "deal_links"),
        Rule(contentlink,callback= "parse_item"),
    )


    #links 是当前response 提取出来的链接列表
    #Type&page=xxx?type=4 修改为 Type?page=xxx&type=4
    def deal_links(self,links):
        for each in links:
            each.url = each.url.replace("?","&").replace("Type&","Type?")
        return links



    def parse_item(self, response):
        item = DongguanItem()

        #标题
        item["title"] = response.xpath('//div[@class="pagecenter p3"]//strong//text()').extract()[0]
        #编号
        item["number"] = item["title"].split('.')[-1].split(":")[-1]
        #内容(返回是一个列表) 如果有内用，则返回列表，无无内容则返回为空列表
        content = response.xpath('//div[@class="contentext"]/text()').extract()

        #如果没内用，则是使用无图片的的匹配的规则 (有图片与无图片的是有区别的)
        if len(content) == 0:
            content = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            item["content"] = "".join(content).strip()
        else:
            item["content"] = "".join(content).strip()



        #链接
        item["url"] = response.url

        yield item
