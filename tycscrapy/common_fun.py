import os
import redis
import pymysql
import codecs
import time

# 爬取的html文件的文件夹
# BASE_PATH = "/Users/tangtonglong/fsdownload/shops"
BASE_PATH = "/Users/tangtonglong/Downloads/shops"

# 保存json格式的店铺信息
DETAIL_FILE = 'shop_detail.json'
# json格式的评论信息
COMMENT_FILE = 'comment_list.json'

# json格式的公司信息
COMPANY_FILE = 'company_list.json'

# 没有index的店铺集合
SHOP_NOT_FOUND_SET = 'dianping:shop:notfound'

# index.html中的内容是列表页，不是店铺详情的集合
SHOP_NOT_INDEX_SET = 'dianping:shop:notindex'

# 店铺id集合
SHOP_SET = 'dianping:shop'
# 店铺详情转换成功的
DETAIL_SUCCESS_SET = 'dianping:shop:detail:success'
# 店铺详情转换失败的
DEATIL_FAILED_SET = 'dianping:shop:detail:fail'
# 评论详情转换成功的
COMMENT_SUCCESS_SET = 'dianping:shop:comment:success'
# 评论详情转换失败的
COMMENT_FAILED_SET = 'dianping:shop:comment:fail'

# 没有comment的店铺集合
COMMENT_NOT_FOUND_SET = 'dianping:shop:comment:notfound'

# 店铺id:店铺名
SHOP_NAME_MAP = 'dianping:shop:name'

# 店铺名
SHOP_NAME_SET = 'shopname'

# 点评 : 天眼查的map { 点评店铺id : 天眼查公司id }
DIANPING_TIANYANCHA_MAP = 'dianping:tianyacha'

# 天眼查公司id
TYC_COMPANY_SET = 'tianyancha:company'
# 天眼查解析成功的店铺集合(天眼查的公司id集合)
TYC_SUCCESS_SET = 'tianyancha:company:success'
# 天眼查解析失败的店铺集合(天眼查的公司id集合)
TYC_FAILED_SET = 'tianyancha:company:fail'

# shop:品牌链接 map
SHOP_BRAND_MAP = 'shop:brand'
# 有品牌的shop的集合（其实也是从shop名搜索brand成功的集合）
SHOP_HAVE_BRAND_SET = 'shop:brand:have'
# 没有品牌的shop的集合（其实也是从shop名搜索brand失败的集合）
SHOP_NOT_HAVE_BRAND_SET = 'shop:brand:nothave'

# 店铺和公司的对应map
SHOP_COMPANY_MAP2 = 'shop:company'
# 公司解析成功的
SHOP_COMPANY_SUCCESS = 'shop:company:success'
# 公司解析失败的
SHOP_COMPANY_FAILED = 'shop:company:failed'

# 品牌和公司的对应map
BRAND_COMPANY_MAP = 'brand:company'

# shopid:店铺名--关键字

# 关键字:品牌名--id
KEYWORD_BRAND_MAP = 'keyword:brand'
# shopid:关键字
SHOP_KEYWORD = 'shopkeyword'

# 排除的品牌的名称
BRAND_EXCLUDE = 'brand:exclude'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379


def get_fold_name(file_dir):
    return os.listdir(file_dir)


def get_indexhtml_path(dirname):
    return BASE_PATH + '/' + dirname


def get_redis_conn():
    pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT)
    redis_cli = redis.StrictRedis(connection_pool=pool, port=6379, db=0, password=None, encoding='utf-8',
                                  decode_responses=True)
    return redis_cli


def save_item_to_file(filename, item):
    with codecs.open(filename, 'a', encoding='utf8') as f:
        f.write(item)


def get_cur_time_str():
    return time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())


def get_mysql_data(sqlstat, columnlist):
    db = pymysql.connect("localhost", "root", "12345678", "testdb", charset='utf8')
    # 使用cursor()方法获取操作游标

    try:
        cursor = db.cursor()
        resultdictlist = []
        itemdict = {}
        # 执行SQL语句
        cursor.execute(sqlstat)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            for i in range(0, len(results)):
                itemdict[columnlist[i]] = row[i]
                print(itemdict[columnlist[i]])
            resultdictlist.append(itemdict)
        # 打印结果
        # print ("region_Code=%s,region_Name=%s,regionLevel=%s,pid=%s,pid_path=%s" % (region_Code, region_Name, regionLevel, pid, pid_path )
        return resultdictlist
    except:
        print("Error: unable to fecth data")
        return None


def main():
    redi_cli = get_redis_conn()
    shop_name = redi_cli.smembers(SHOP_NAME_SET)
    for ele in shop_name:
        # print(ele.decode()+':')
        print(ele.decode())
        save_item_to_file("shopname.txt", ele.decode() + '\n')
    notfoundlist = redi_cli.smembers(COMMENT_NOT_FOUND_SET)
    for ele in notfoundlist:
        # print(ele.decode()+':')
        print(ele.decode())
        save_item_to_file("notfoundcomment.txt", ele.decode() + '\n')


#     dir_list = get_fold_name('/Users/tangtonglong/fsdownload/shops')
#     indexhtml_path = get_indexhtml_path(dir_list[0])
#     print(indexhtml_path)

if __name__ == '__main__':
    main()