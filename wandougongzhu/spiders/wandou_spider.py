import time

import scrapy, re, io, sys


# 改变默认输出编码
import json

from wandougongzhu.items import WandougongzhuItem


class woniuSplider(scrapy.Spider):
    name = "wandou_spider"
    cat_ids = 0
    def start_requests(self):
        headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'cookie': 'user_key=84702303b89bbac242f622b4deafb53e',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
                   'referer': 'https://m.wandougongzhu.cn/category/cat?cat_id=values',
                   'origin': 'https://m.wandougongzhu.cn',
                   'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
                   }
        url = "https://m.wandougongzhu.cn/list/ajaxGoods"
        #目前获取不到共有几页  太复杂 直接设置页数
        for cat_id in range(450,452):
            self.cat_ids = cat_id
            headers['referer'] = str(headers['referer']).replace("values",str(cat_id))
            time.sleep(3)
            for i in range(1, 10):
                myFormData = {
                    'brand': '',
                    'cat_id': str(cat_id),
                    'page': str(i),
                    'sort': 'general',
                    'promote': '',
                    'seller': '',
                    'count': '20',
                    'cat': str(cat_id),
                }

                yield scrapy.FormRequest(url,callback=self.parse_item,formdata=myFormData,headers=headers)


    def parse_item(self,response):
        body = response.body.decode('utf-8')
        body_dict = json.loads(body, strict=False)
        data_list = body_dict['data']['goods']['list']
        if data_list:
            for data in data_list:
                wandou_item = WandougongzhuItem()
                wandou_item['goods_slogan'] = data['slogan']
                wandou_item['brand_name'] = data['brand_name']
                wandou_item['goods_price'] = str(data['final_price'])
                wandou_item['goods_title'] = data['goods_name']
                wandou_item['cat_id'] = str(self.cat_ids)
                yield wandou_item


