# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WandougongzhuItem(scrapy.Item):
    goods_slogan = scrapy.Field()

    goods_title = scrapy.Field()

    goods_price = scrapy.Field()

    brand_name = scrapy.Field()

    cat_id = scrapy.Field()