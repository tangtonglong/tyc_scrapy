# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TycscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    shop_id = scrapy.Field()

    shop_name = scrapy.Field()

    shop_keywords = scrapy.Field()

    # 品牌名
    brand_name = scrapy.Field()
    # 品牌链接
    brand_href = scrapy.Field()
    # 品牌id
    brand_id = scrapy.Field()


class company_detail(scrapy.Item):

    # 搜索词
    search_key = scrapy.Field()
    # 公司id
    company_id = scrapy.Field()
    # 公司名
    company_name = scrapy.Field()
    # 公司照片
    company_img = scrapy.Field()
    # 公司电话
    company_tel = scrapy.Field()
    # 详细地址
    company_address = scrapy.Field()
    # 邮箱
    company_email = scrapy.Field()
    # 官网
    company_net_address = scrapy.Field()
    # 公司简介
    company_desc = scrapy.Field()
    # 公司工商信息
    company_business_info = scrapy.Field()
    # 经营风险
    company_manageDangerous = scrapy.Field()
    # 经营状况
    company_manageStatus = scrapy.Field()

    company_tel_email_address = scrapy.Field()

