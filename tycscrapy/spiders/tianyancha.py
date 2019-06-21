# -*- coding: utf-8 -*-
import urllib.parse

import lxml.html as HTML
import scrapy

from tycscrapy.common_fun import save_item_to_file
from tycscrapy.config import get_cookies
from tycscrapy.items import company_detail


class TianyanchaSpider(scrapy.Spider):
    name = 'tianyancha'
    allowed_domains = ['tianyancha.com']

    with open('./spiders/search_key.txt', 'r', encoding='utf-8') as f:
        file = f.readlines()

    with open('./spiders/success', 'r', encoding='utf-8') as e:
        s_file = e.readlines()
    # 成功的关键字的集合
    success_set = set()
    for e in s_file:
        success_set.add(e.replace('\n', '').replace(' ', ''))
    # 待搜索的关键字dict
    search_key_set = set()
    for ele in file:
        tmp = ele.replace('\n', '').replace(' ', '')
        if len(tmp) > 0:
            search_key_set.add(ele.replace('\n', '').replace(' ', ''))

    diff_set = search_key_set - success_set
    print('search_set总大小：' + str(len(search_key_set)))
    print('diff_set总大小：' + str(len(diff_set)))

    url_prefix = 'https://www.tianyancha.com/search?key='
    start_urls = []
    for ele in diff_set:
        start_urls.append(url_prefix + ele)



    def parse(self, response):
        # collect `item_urls`

        search_key = urllib.parse.unquote(response.url.split("=")[-1])

        # brand_item = TycscrapyItem()
        # isSuccessed = False

        # brand_href_dom = response.xpath(
        #     '//a[contains(@class,"brand sv-search-company-brand") and contains(@data-id,"t1")]/@href')
        #
        # if len(brand_href_dom) > 0:
        #     brand_item["brand_href"] = brand_href_dom.extract_first()
        #     brand_item["brand_id"] = brand_href_dom.extract_first().split("/")[-1]
        #     isSuccessed = True
        # else:
        #     # print(keywords+" 无品牌 ！！！")
        #     pass
        #
        # brand_name_dom = response.xpath(
        #     '//span[contains(@class,"tag-common -primary-bg") and contains(text(),"项目品牌")]/preceding-sibling::span[1]/@title')
        # if len(brand_name_dom) > 0:
        #     brand_item["brand_name"] = brand_name_dom.extract_first()
        #     isSuccessed = True
        # else:
        #     pass
        # if isSuccessed and not self.redis_cli.sismember(BRAND_EXCLUDE, brand_item["brand_name"]):
        #     print(search_key + " -- " + brand_item["brand_name"] + ' -- ' + brand_item["brand_id"])
        #     save_item_to_file("keyword-brand.txt",search_key + " -- " + brand_item["brand_name"] + ' -- ' + brand_item["brand_id"] + "\n")
        #     self.redis_cli.hset(KEYWORD_BRAND_MAP, search_key, brand_item["brand_name"] + ' -- ' + brand_item["brand_id"])
        #     yield brand_item

        search_company = []
        # result_list_dom = response.xpath( '//div[@class = "result-list sv-search-container"]/div[@class="search-item sv-search-company"]/div[contains(@class,"search-result-single")]')
        result_list_dom = response.xpath('//div[@class = "result-list sv-search-container"]/div[@class="search-item sv-search-company"]/div[contains(@class,"search-result-single")]/div[@class = "content"]/div/a/@href')
        result_list_dom2 = response.xpath(
            '//div[@class = "result-list sv-search-container"]/div[@class="search-item sv-search-company"]/div[contains(@class,"search-result-single")]/div[@class = "content"]/div/a/em/text()')
        if len(result_list_dom) > 0:
            company_result = company_detail()
            com_href = result_list_dom[0].extract()
            company_result['company_id'] = str(com_href).split('/')[-1]
            company_result['company_net_address'] = com_href
            company_result['search_key'] = search_key

            if len(result_list_dom2) > 0:
                com_name = result_list_dom2[0].extract()
                com_name = str(com_name).strip().replace('\n', '').replace("\t", "").replace(" ", "")
                company_result['company_name'] = com_name
            print('search_key : ' + search_key + 'company_name : ' + company_result['company_name'])
            save_item_to_file('./spiders/success', search_key + '\n')
            yield company_result
        else:
            print('failed : ' + search_key)
            save_item_to_file('./spiders/fail', search_key + '\n')







    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=get_cookies())

    def get_brand_href(responsetext):
        # url = 'https://www.tianyancha.com/search?key=' + keywords
        # c = download_page(url)
        html = HTML.fromstring(responsetext)

        brand_href = ''
        brand_dom = html.xpath(
            '//a[contains(@class,"brand sv-search-company-brand") and contains(@data-id,"t1")]/@href')
        if len(brand_dom) > 0:
            brand_href = brand_dom[0]
        else:
            # print(keywords+" 无品牌 ！！！")
            return None

        brand_name = ''
        brand_name_dom = html.xpath(
            '//span[contains(@class,"tag-common -primary-bg") and contains(text(),"项目品牌")]/preceding-sibling::span[1]/@title')
        if len(brand_name_dom) > 0:
            brand_name = brand_name_dom[0]
        else:
            return None

        return brand_name + '￥' + brand_href