
from tycscrapy.common_fun import get_redis_conn,KEYWORD_BRAND_MAP

NAME_KEY_WORDS_REPLACE = ("学习", "教育", "青少儿", "培训", "国际", "少儿", "幼儿", "儿童", "学校",)

NAME_KEY_WORDS = ("英语", "口语", "外语", "外教", "艺术", "表演",)

# 过滤掉无效的关键词
def filter_shop_name(shopname):
    shopname_temp = shopname.split("(")[0].replace("学习","").replace("英语","")
    for ele in NAME_KEY_WORDS_REPLACE:
        if shopname_temp.find(ele) > 0:
            shopname_temp = shopname_temp[0:shopname_temp.find(ele)]
            break
        else:
            pass
    return shopname_temp

# 判断是否需要去搜索
def exists_keys(shopname):
    for ele in NAME_KEY_WORDS:
        if shopname.find(ele) > 0:
            return True
        else:
            pass
    return False

# 关键字是否需要搜索
# 关键字:品牌id
# KEYWORD_BRAND_MAP = 'keyword:brand'
def isNeedSearch(keywords):
    redis_cli = get_redis_conn()
    if redis_cli.hexists(KEYWORD_BRAND_MAP, keywords):
        # 关键字已经有匹配到的品牌 不需要再搜索
        return False
    else:
        return True

