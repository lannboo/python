# -*- coding: utf-8 -*-
import scrapy

from scrapy.spiders import Spider

from dongguan.items import DongguanItem


class SunSpider(Spider):
    name = 'xixi'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://d.wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url +str(offset)]



    #
    def parse(self, response):
        #每一页里的所有帖子的链接的集合

        links = response.xpath('//div[@class="greyframe"]/table//td/a[@class="news14"]/@href').extract()
        for link in links:
            #提取列表里的每一个帖子的链接，并发送请求的调用 parse_item 来处理
            yield  scrapy.Request(link,callback=self.parse_item)


        if self.offset <= 93330:
            self.offset += 30
            #发送请求放到请求队列里，调用 self.parse 来处理
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)
        print(response.body)


    #处理每个帖子的链接
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

        #放到管道文件
        yield item
