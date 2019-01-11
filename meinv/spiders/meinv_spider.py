# -*- coding: utf-8 -*-
import scrapy
from meinv.items import MeinvItem

class MeinvSpiderSpider(scrapy.Spider):
    name = 'meinv_spider'
    allowed_domains = ['27270.com']
    start_urls = [
        'https://www.27270.com/ent/meinvtupian/2019/313847.html',
        'https://www.27270.com/ent/meinvtupian/2019/313844.html',
        'https://www.27270.com/ent/meinvtupian/2019/313832.html'
    ]

    def parse(self, response):
        meinv_item = MeinvItem()
        meinv_item['title'] = response.xpath("/html/body/div[2]/div[2]/h1/text()").extract_first()
        meinv_item['imgurl'] = response.xpath("//*[@id='picBody']/p/a[1]/img/@src").extract_first()
        yield meinv_item

        next_link = response.xpath("//*[@id='nl']/a/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://www.27270.com/ent/meinvtupian/2019/"+next_link,callback=self.parse)
