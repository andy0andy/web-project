import requests
import pymongo
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


'''
图书网站，无反爬，数据通过 Ajax 加载，有翻页，适合大批量动态页面渲染抓取。
'''


url = "https://spa5.scrape.center/api/book/?limit=18&offset={}"
detail_url = "https://spa5.scrape.center/api/book/{}/"


# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r



# 获得url
def get_url():
    for i in range(0,9200,18):

        page_url = url.format(i)
        yield page_url



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

    item['authors'] = js_data['authors']
    item['catalog'] = js_data['catalog']
    item['comments'] = js_data['comments']
    item['cover'] = js_data['cover']
    item['introduction'] = js_data['introduction']
    item['isbn'] = js_data['isbn']
    item['name'] = js_data['name']
    item['price'] = js_data['price']
    item['published_at'] = js_data['published_at']
    item['publisher'] = js_data['publisher']
    item['score'] = js_data['score']
    item['tags'] = js_data['tags']
    item['translators'] = js_data['translators']
    item['url'] = js_data['url']


    return item



def work(t):
    url,coll = t

    js_data = get_json(url)

    for one_data in js_data['results']:

        id = one_data['id']
        d_url = detail_url.format(id)

        jd = get_json(d_url)

        item = parse_detail(jd)



        # print(item)
        r = save_mongo(item,coll)
        print(r)


def run(coll):
    pool = ThreadPoolExecutor(max_workers=8)

    pool.map(work,[(url,coll) for url in get_url()])


if __name__ == '__main__':
    run('spa5')