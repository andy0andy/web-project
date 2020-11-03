import requests
import pymongo
from concurrent.futures import ThreadPoolExecutor
import time
import hashlib
import base64


'''
电影数据网站，无反爬，数据通过 Ajax 加载，数据接口参数加密且有时间限制，适合动态页面渲染爬取或 JavaScript 逆向分析。
'''


url = "https://spa2.scrape.center/api/movie/?limit=10&offset={}&token={}"


# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r


# python 代码复现 js 加密函数
def i():
    arguments = "/api/movie"

    t = str(round(int(time.time()*1000) / 1000))

    r = [arguments,t]

    o = hashlib.sha1(','.join(r).encode('utf-8')).hexdigest()

    c = base64.b64encode(','.join([o,t]).encode('utf-8'))
    c = str(c).lstrip("b'").rstrip("'")

    return c


# 得到token
def get_token():
    tk = i()

    return tk




# 获得url
def get_url():
    token = get_token()

    for i in range(0,100,10):


        detail_url = url.format(i,token)
        yield detail_url



# 返回json
def get_json(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    js_data = r.json()

    return js_data



# 返回字典类型数据
def parse_detail(js_data):



    item = {}

    item['title'] = js_data['name'] + " - " + js_data['alias']
    item['score'] = js_data['score']
    item['tags'] = js_data['categories']
    item['addr'] = js_data['regions']
    item['time'] = js_data['minute']
    item['show'] = js_data['published_at']
    item['cover'] = js_data['cover']


    return item



def work(t):
    url,coll = t

    js_data = get_json(url)

    for one_data in js_data['results']:
        item = parse_detail(one_data)

        r = save_mongo(item,coll)
        print(r)


def run(coll):
    pool = ThreadPoolExecutor(max_workers=8)

    pool.map(work,[(url,coll) for url in get_url()])


if __name__ == '__main__':
    run('spa2')
