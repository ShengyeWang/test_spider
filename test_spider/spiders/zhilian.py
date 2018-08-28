# -*- coding: utf-8 -*-
import scrapy


class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    #allowed_domains = ['zhilian.com']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        print(response.body)
        pass
