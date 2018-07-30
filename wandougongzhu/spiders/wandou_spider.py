import scrapy, re, io, sys


# 改变默认输出编码
import json

from wandougongzhu.items import WandougongzhuItem


class woniuSplider(scrapy.Spider):
    name = "wandou_spider"
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'cookie': 'ch=bdsem_pc; user_key=caa79cc27517c8b1aef82ae9dc49d278; UM_distinctid=164da8a2564992-0651de478967de-514d2f1f-1fa400-164da8a25663f; img_fmt=webp; wct=bdsem_pc; CNZZDATA1257364836=195384166-1532760695-https%253A%252F%252Fm.wandougongzhu.cn%252F%7C1532922988',
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36',
               'referer':'https://m.wandougongzhu.cn/category/cat?cat_id=426',
               'origin':'https://m.wandougongzhu.cn',
               'content-type':'application/x-www-form-urlencoded; charset=UTF-8'
               }
    def start_requests(self):
        url = "https://m.wandougongzhu.cn/list/ajaxGoods"
        myFormData = {'brand': '',
                      'cat_id': '426',
                      'page': '1',
                      'sort': 'general',
                      'promote': '',
                      'seller': '',
                      'count': '20',
                      'cat': '426',
                      }
        yield scrapy.FormRequest(url,callback=self.parse_item,formdata=myFormData,headers=self.headers)


    def parse_item(self,response):
        body = response.body.decode('utf-8')
        body_dict = json.loads(body, strict=False)
        for data in body_dict['data']['goods']['list']:
            wandou_item = WandougongzhuItem()
            wandou_item['goods_slogan'] = data['slogan']
            wandou_item['brand_name'] = data['brand_name']
            wandou_item['goods_price'] = str(data['final_price'])
            wandou_item['goods_title'] = data['goods_name']
            yield wandou_item


