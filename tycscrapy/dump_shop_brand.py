# -*- coding: utf-8 -*-
import scrapy
from tycscrapy.config import get_cookies
from tycscrapy.common_fun import get_redis_conn,SHOP_NAME_MAP,SHOP_KEYWORD,KEYWORD_BRAND_MAP,BRAND_EXCLUDE,save_item_to_file
import lxml.html as HTML
import lxml.etree as etree
from tycscrapy.items import TycscrapyItem,company_detail
from tycscrapy.tyc_filters import filter_shop_name,exists_keys,isNeedSearch
import urllib.parse

def dump_shop_brand():
    redis_cli = get_redis_conn()
    shop_name_dict = redis_cli.hgetall(SHOP_NAME_MAP)
    shop_keyword_dict = {}
    for ele in shop_name_dict:
        shop_keyword_dict[ele.decode()] = filter_shop_name(shop_name_dict[ele].decode())

    for ele in shop_keyword_dict:
        item_str = ele + ' -- ' + redis_cli.hget(SHOP_NAME_MAP, ele).decode() + ' -- ' + shop_keyword_dict[ele] + ' -- '
        if redis_cli.hexists(KEYWORD_BRAND_MAP, shop_keyword_dict[ele]):
            item_str += redis_cli.hget(KEYWORD_BRAND_MAP, shop_keyword_dict[ele]).decode()
        save_item_to_file('shop-name-keys-brand', item_str + '\n')

def main():
    dump_shop_brand()

if __name__ == '__main__':
    main()