# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TycscrapyPipeline(object):
    # def process_item(self, item, spider):
    #     return item
    """
        功能：保存item数据
    """
    def __init__(self):
        # 打开文件
        self.filename = open("company.json", "w", encoding='utf-8')

    def process_item(self, item, spider):
        # 将获取到的每条item转换为json格式
        text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.filename.write(text)
        return item

    def close_spider(self, spider):
        # 关闭文件
        self.filename.close()