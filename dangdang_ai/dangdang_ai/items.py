# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangAiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #价格
    price = scrapy.Field()
    #作者
    author = scrapy.Field()
    #日期
    date = scrapy.Field()
    #出版社
    location = scrapy.Field()
    #星级
    star = scrapy.Field()
    #评论
    review = scrapy.Field()
    #简介
    introduce = scrapy.Field()
