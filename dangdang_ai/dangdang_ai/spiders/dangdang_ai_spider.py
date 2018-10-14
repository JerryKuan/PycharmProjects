# -*- coding: utf-8 -*-
import scrapy
from dangdang_ai.items import DangdangAiItem

class DangdangAiSpiderSpider(scrapy.Spider):
    name = 'dangdang_ai_spider'
    allowed_domains = ['category.dangdang.com']
    start_urls = ['http://category.dangdang.com/cp01.54.92.00.00.00.html']

    def parse(self, response):
        #爬取第一页列表
        book_list = response.xpath("//div[@class='con shoplist']//div[@id='search_nature_rg']//ul[@class='bigimg']/li")
        # print(book_list)
        for i_book_list in book_list:
            #解析数据
            dangdang_ai_item= DangdangAiItem()
            dangdang_ai_item['price'] = i_book_list.xpath(".//p[@class='price']//span[1]/text()").extract_first()
            dangdang_ai_item['author'] = i_book_list.xpath(".//p[@class='search_book_author']//span[1]/a/text()").extract_first()
            dangdang_ai_item['date'] = i_book_list.xpath(".//p[@class='search_book_author']//span[2]/text()").extract_first()
            dangdang_ai_item['location'] = i_book_list.xpath(".//p[@class='search_book_author']//span[3]/a/text()").extract_first()
            dangdang_ai_item['star'] = i_book_list.xpath(".//p[@class='search_star_line']//span[@class='search_star_black']/span/@style").extract_first()
            dangdang_ai_item['review'] = i_book_list.xpath(".//p[@class='search_star_line']//a/text()").extract_first()
            dangdang_ai_item['introduce'] = i_book_list.xpath(".//p[@class='detail']/text()").extract_first()
            # print(dangdang_ai_item)
            #将数据yield到pipline
            yield dangdang_ai_item
        # 爬取剩余页
        next_page = response.xpath("//div[@class='paging']//ul[@name='Fy']//li[@class='next']//a//@href").extract()

        if next_page:
            next_page = next_page[0]
            yield scrapy.Request('http://category.dangdang.com/'+next_page,callback=self.parse)
