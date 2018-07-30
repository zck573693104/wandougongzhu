from scrapy import cmdline
cmdline.execute('scrapy crawl wandou_spider -o info.csv -t csv'.split())