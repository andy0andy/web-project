import requests
from faker import Faker
import execjs
import os

fake = Faker()


class BaiduFanyi(object):

    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi"


    def _get_sign(self, q):
        with open(os.path.join(os.getcwd(), os.path.join("baiduFanyi", "script.txt")), 'r', encoding='utf-8') as f:
            comp = execjs.compile(f.read())

        res = comp.call('e', q)

        return res  

    def fanyi(self, q, f, t):

        headers = {
            "User-Agent": fake.user_agent(),
            "origin": "https://fanyi.baidu.com",
            "referer": "https://fanyi.baidu.com/",
            'cookie': "BIDUPSID=058FF67C1E41830D036DCC024704AD54; PSTM=1603436052; BAIDUID=058FF67C1E41830D302E5B181B86780C:FG=1; BAIDUID_BFESS=058FF67C1E41830D302E5B181B86780C:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1605863699,1605864632; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1605864632; __yjsv5_shitong=1.0_7_69547790712b9c30777073227f6b60d05d89_300_1605864632862_119.139.196.92_d502103c; yjs_js_security_passport=8bdb64dcd17d75aadea6e8c190f74f5c050c5215_1605864633_js",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "content-length": "136",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-",
            "x-requested-with": "XMLHttpRequest",
        }

        params = {
            'from': f,
            'to': t
        }


        form_data = {
            "from": f,
            "to": t,
            "query": q,
            "transtype": "realtime" ,
            "simple_means_flag": "3",
            "sign": self._get_sign(q),
            "token": "1b9167c7d415ba2afc38e3046da35e1e",
            "domain": "common",
        }


        response = requests.post(self.url, headers=headers, params=params, data=form_data)
        res = response.json()

        data = res['trans_result']['data'][0]

        # print(data)

        return data['dst']



if __name__ == '__main__':
    baidfanyi = BaiduFanyi()

    r = baidfanyi.fanyi("apple",'en','zh')

    print(r)
