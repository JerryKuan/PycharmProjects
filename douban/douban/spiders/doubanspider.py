# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
from scrapy.selector import Selector
from scrapy.http import Request


class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanspider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # 实例化item
        item = DoubanItem()
        base = response.xpath("//ol[@class='grid_view']/li")
        # print(base)
        for i_item in base:
            item['name'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='hd']//a/span[1]/text()").extract_first()
            item['actor'] = i_item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()[1]").extract_first().strip().replace("\n","").replace("\xa0","")
            item['info'] = i_item.xpath(".//div[@class='item']/div[@class='info']/div[@class='bd']/p[1]/text()[2]".strip()).extract_first().strip().replace("\n","").replace("\xa0","")
            item['star'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']//span[2]/text()").extract_first()
            item['evaluate'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//div[@class='star']//span[4]/text()").extract_first()
            item['introduction'] = i_item.xpath(".//div[@class='item']//div[@class='info']//div[@class='bd']//p[@class='quote']/span/text()").extract_first()
            yield item
            print(item)

        nextpage = response.xpath("//*[@id='content']/div/div[1]/div[2]/span[3]/a/@href").extract_first()
        if nextpage:
            yield Request(url='https://movie.douban.com/top250'+nextpage,callback = self.parse)
