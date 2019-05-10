# -*- coding: utf-8 -*-
#
# # Define here the models for your spider middleware
# #
# # See documentation in:
# # https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#
# from scrapy import signals
#
#
# class TencentspiderSpiderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.
#
#         # Should return None or raise an exception.
#         return None
#
#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.
#
#         # Must return an iterable of Request, dict or Item objects.
#         for i in result:
#             yield i
#
#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.
#
#         # Should return either None or an iterable of Response, dict
#         # or Item objects.
#         pass
#
#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.
#
#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)
#
#
# class TencentspiderDownloaderMiddleware(object):
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s
#
#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.
#
#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None
#
#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.
#
#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response
#
#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.
#
#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass
#
#     def spider_opened(self, spider):
#         spider.logger.info('Spider opened: %s' % spider.name)

from settings import USER_AGENTS
import random
import time
import requests
import base64


# User-Agetn 下载中间件
class RandomUserAgent(object):
    def process_request(self, request, spider):
        # 这句话用于随机选择user-agent
        user_agent = random.choice(USER_AGENTS)
        date = time.strftime(u"%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
        #print user_agent
        request.headers.setdefault('User-Agent', user_agent)
        #request.headers.setdefault('If-Modified-Since', date)

class RandomProxy(object):
    def __init__(self):
        #self.proxy_list = ["121.40.108.76:80", "121.8.243.51:8888","221.204.116.169:9797","112.95.205.29:8888","183.31.254.57:9797","221.204.116.211:9797"]
        self.proxy_auth = "mr_mao_hacker:sffqry9r"
        self.proxy_api = "http://dps.kuaidaili.com/api/getdps/?orderid=958655825381063&num=50&ut=1&sep=3"
        self.proxy_list = requests.get(self.proxy_api).text.split()

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy_list)
        base64_userpass = base64.b64encode(self.proxy_auth)
        #print proxy
        request.meta['proxy'] = "http://" + proxy
        #if self.proxy_auth != None:
        request.headers['Proxy-Authorization'] = "Basic " + base64_userpass


#class ProxyMiddleware(object):
    # overwrite process request
    #def process_request(self, request, spider):
        # Set the location of the proxy
    #    sql = 'select ip,port from t_proxy_ip t where t.is_valid =1'
    #    result = SqlUtil.query_all(sql)
    #    ip_port = random.choice(result)
    #    logging.info(ip_port)
    #    request.meta['proxy'] = "http://{0}:{1}".format(ip_port['ip'], ip_port['port'])
        # # Use the following lines if your proxy requires authentication
        # proxy_user_pass = "USERNAME:PASSWORD"
        # # setup basic authentication for the proxy
        # encoded_user_pass = base64.encodestring(proxy_user_pass)
        # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass



