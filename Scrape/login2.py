import requests
from lxml import etree
import pymongo
from concurrent.futures import ThreadPoolExecutor


'''
对接 Session + Cookies 模拟登录，适合用作 Session + Cookies 模拟登录练习。
'''


url = "https://login2.scrape.center/detail/{}"

ck = {
    "sessionid": "ue27m5amd0v2q8h6w4v729w64xwinxyy"
}

s = requests.session()


# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r



# 获得url
def get_url():
    for i in range(1,101):

        detail_url = url.format(i)
        yield detail_url



# 返回json
def get_data(url):
    r = s.get(url,cookies=ck)

    if r.status_code != 200:
        return None

    data = r.text

    return data



# 返回字典类型数据
def parse_detail(data):
    html = etree.HTML(data, parser=etree.HTMLParser())

    item = {}

    item['title'] = html.xpath("//h2[@class='m-b-sm']/text()")[0].replace('\n','').replace(' ','')
    item['score'] = html.xpath("//p[@class='score m-t-md m-b-n-sm']/text()")[0].replace('\n','').replace(' ','')
    item['tags'] = html.xpath("//div[@class='categories']//span/text()")
    item['addr'] = html.xpath("//div[@class='m-v-sm info'][1]/span[1]/text()")[0].replace('\n','').replace(' ','')
    item['time'] = html.xpath("//div[@class='m-v-sm info'][1]/span[3]/text()")[0].replace('\n','').replace(' ','')
    item['show'] = html.xpath("//div[@class='m-v-sm info'][2]/span[1]/text()")[0].replace('\n','').replace(' ','')
    item['cover'] = html.xpath("//div[@class='drama']/p/text()")[0].replace('\n','').replace(' ','')

    return item



def work(t):
    url,coll = t

    data = get_data(url)

    item = parse_detail(data)

    r = save_mongo(item,coll)
    print(r)


def run(coll):
    pool = ThreadPoolExecutor(max_workers=8)

    pool.map(work,[(url,coll) for url in get_url()])


if __name__ == '__main__':
    run('login2')
