# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors

from dangdang_ai.settings import MYSQL_HOST,MYSQL_DBNAME,MYSQL_USER,MYSQL_PASSWORD

class DangdangAiPipeline(object):

    def __int__(self):
        #数据库配置信息
        self.connect = pymysql.connect(
            host = MYSQL_HOST,
            db = MYSQL_DBNAME,
            user = MYSQL_USER,
            password = MYSQL_PASSWORD,
            charset = 'utf8',
            use_unicode = True,
        )
        #通过cursor进行增删改查
        self.cursor = self.connect.cursor()



    def process_item(self, item, spider):
        try:
            #查重处理
            self.cursor.execute(
                """select * from book_dangdang_ai_info WHERE  review = %s""",item['review'])
            #是否重复
            repetition = self.cursor.fetchone()

            if repetition:
                pass
            else:
                #插入数据
                self.cursor.execute("""insert into book_dangdang_ai_info (price,author,date,location,star,review,introduce) values(%s,%s,%s,%s,%s,%s,%s)""",
                     (item['price'],
                      item['author'],
                      item['date'],
                      item['location'],
                      item['star'],
                      item['review'],
                      item['introduce']))
            self.connect.commit()
        except Exception as error:
            print(error)
        return item

