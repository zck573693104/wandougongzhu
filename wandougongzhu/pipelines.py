from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
from scrapy.crawler import Settings as settings
class WandougongzhuPipeline(object):
    quotesInsert = '''insert into wandou(title,price,name,brand)
                            values('{goods_title}','{goods_price}','{goods_slogan}','{brand_name}')'''

    def __init__(self, settings):
        self.settings = settings

    def process_item(self, item, spider):
        print(item)
        if spider.name == "wandou_spider":
            sqltext = self.quotesInsert.format(
                goods_title=pymysql.escape_string(item['goods_title']),
                goods_price=pymysql.escape_string(item['goods_price']),
                goods_slogan=pymysql.escape_string(item['goods_slogan']),
                brand_name=pymysql.escape_string(item['brand_name']))
            self.cursor.execute(sqltext)

        else:
            spider.log('Undefined name: %s' % spider.name)

        return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def open_spider(self, spider):
        # 连接数据库
        self.connect = pymysql.connect(
            host=self.settings.get('MYSQL_HOST'),
            port=self.settings.get('MYSQL_PORT'),
            db=self.settings.get('MYSQL_DBNAME'),
            user=self.settings.get('MYSQL_USER'),
            passwd=self.settings.get('MYSQL_PASSWD'),
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
        self.connect.autocommit(True)

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()