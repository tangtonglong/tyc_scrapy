import time
import requests
from random import randint

class CommonCrawler:
    timeout = 10
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
        'Host': 'www.tianyancha.com'
    }

    def get_cookies(self):
        # s = "showNav=#nav-tab|0|1; navCtgScroll=0; navCtgScroll=158; showNav=#nav-tab|0|1; cy=2; cye=beijing; _lxsdk_cuid=16aa04adfc7c8-00cd3c2dcc926a-3b720b58-1fa400-16aa04adfc7c8; _lxsdk=16aa04adfc7c8-00cd3c2dcc926a-3b720b58-1fa400-16aa04adfc7c8; _hc.v=d71b149e-d310-b132-6a83-6f0b513eed3e.1557467423; s_ViewType=10; aburl=1; wed_user_path=33780|0; _lxsdk_s=16aa0a32636-7fa-7d2-f16%7C%7C730"
        s = "ssuid=830453994; TYCID=59f917606b1611e9b83e5dde1d37d7df; undefined=59f917606b1611e9b83e5dde1d37d7df; _ga=GA1.2.137816161.1556607978; tyc-user-info=%257B%2522claimEditPoint%2522%253A%25220%2522%252C%2522myAnswerCount%2522%253A%25220%2522%252C%2522myQuestionCount%2522%253A%25220%2522%252C%2522signUp%2522%253A%25220%2522%252C%2522explainPoint%2522%253A%25220%2522%252C%2522privateMessagePointWeb%2522%253A%25220%2522%252C%2522nickname%2522%253A%2522%25E7%25B1%25B3%25E6%258B%2589%25C2%25B7%25E7%25B4%25A2%25E7%25BB%25B4%25E8%25AF%25BA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522privateMessagePoint%2522%253A%25220%2522%252C%2522state%2522%253A0%252C%2522announcementPoint%2522%253A%25220%2522%252C%2522isClaim%2522%253A%25220%2522%252C%2522vipManager%2522%253A%25220%2522%252C%2522discussCommendCount%2522%253A%25221%2522%252C%2522monitorUnreadCount%2522%253A%2522185%2522%252C%2522onum%2522%253A%25220%2522%252C%2522claimPoint%2522%253A%25220%2522%252C%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzYyMTA3ODM4OSIsImlhdCI6MTU1NzAyOTYzOCwiZXhwIjoxNTg4NTY1NjM4fQ.9CNMjmVAAjc2L8Ei3qZkMbxQsuvX_FngEuCKAtQnAekVWPwHg0kJqJeLui_yQ7p7RPRcRiDlKCbP_hJJZKeKiQ%2522%252C%2522pleaseAnswerCount%2522%253A%25221%2522%252C%2522redPoint%2522%253A%25220%2522%252C%2522bizCardUnread%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252217621078389%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxNzYyMTA3ODM4OSIsImlhdCI6MTU1NzAyOTYzOCwiZXhwIjoxNTg4NTY1NjM4fQ.9CNMjmVAAjc2L8Ei3qZkMbxQsuvX_FngEuCKAtQnAekVWPwHg0kJqJeLui_yQ7p7RPRcRiDlKCbP_hJJZKeKiQ; __insp_wid=677961980; __insp_slim=1558581899461; __insp_nv=true; __insp_targlpu=aHR0cHM6Ly93d3cudGlhbnlhbmNoYS5jb20vdW5pb25iYWlkdQ%3D%3D; __insp_targlpt=5aSp55y85p_lLeWVhuS4muWuieWFqOW3peWFt1%2FkvIHkuJrkv6Hmga%2Fmn6Xor6Jf5YWs5Y_45p_l6K_iX_W3peWVhuafpeivol%2FkvIHkuJrkv6HnlKjkv6Hmga%2Fns7vnu58%3D; __insp_norec_howoften=true; __insp_norec_sess=true; _gid=GA1.2.1658113203.1558960015; aliyungf_tc=AQAAAC2WuWWmnwgANipFeYeaoGflwdPC; bannerFlag=undefined; csrfToken=SJ5S3oE7EOE7mOLVP4QPS0H5; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1558960013,1558960379,1559098922,1559120037; RTYCID=d5f8e92395494b469f6e7cd7bdc5ca44; CT_TYCID=c7517fa2271f4097b1744021ddfafd1f; cloud_token=34122cf02f62430fa6847c591b50d4b4; cloud_utm=9ba022265dde4851aad4febd9f7541e3; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1559197397; _gat_gtag_UA_123487620_1=1"
        res = {}

        for ele in s.split(';'):
            ele = ele.strip()

            sl = ele.split('=')
            k = sl[0]
            v = '='.join(sl[1:])

            res[k] = v
        return res


    def __init__(self, retries=5):
        self.retries = retries

        self.scheme = 'https'

    def get(self, url):
        tries = 0
        while tries < self.retries:


            try:

                start = time.time() * 1000
                resp = requests.get(url, headers=self.headers, cookies=self.get_cookies(), timeout=10)
                print(self.get_cookies())
                dur = randint(1, 4)
                time.sleep(dur)
                end = time.time() * 1000
                if '你不是机器人' in resp.text:
                    tries += 1
                    print('！！！被封了，快进行验证 ！！！')
                    continue
                else:
                    print('Request succeeded!')
                    return resp.text
            except Exception as e:
                print(e)
                # print('Request failed!The proxy is {}')
                # it's important to feedback, otherwise you may use the bad proxy next time

            tries += 1
        return None
