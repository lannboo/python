# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs

class DongguanPipeline(object):
    def __init__(self):
        # self.filename = codecs.open("dongguan.json", "w",encoding="utf-8")
        self.filename = open("dongguan.json", "w")

    def process_item(self, item, spider):
        #中文默认是使用ascii码来存储，禁用后默认为uncode字符窜
        jsontext = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(jsontext.encode("utf-8"))
        # self.filename.write(jsontext)

    def close_spider(self, spider):
        self.filename.close()
