import requests
from lxml import etree
import pymongo
from concurrent.futures import ThreadPoolExecutor
import time


'''
电影数据网站，无反爬，每个响应增加了 5 秒延迟，适合测试慢速网站爬取或做爬取速度测试，减少网速干扰。
'''

url = "https://ssr4.scrape.center/detail/{}"



# 返回lxml.etree._Element 类型的 html
def get_html(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    html = etree.HTML(r.text,parser=etree.HTMLParser(encoding='utf-8'))

    return html



# 返回字典类型数据
def parse_detail(detail_url):
    d_html = get_html(detail_url)

    item = {}

    try:
        item['title'] = d_html.xpath("//h2[@class='m-b-sm']/text()")[0]
        item['score'] = d_html.xpath("//p[@class='score m-t-md m-b-n-sm']/text()")[0].replace('\n', '').strip()
        item['tags'] = d_html.xpath("//button/span/text()")[:-1]
        item['addr'] = d_html.xpath("//div[@class='m-v-sm info']/span/text()")[0]
        item['time'] = d_html.xpath("//div[@class='m-v-sm info']/span/text()")[2]
        item['show'] = d_html.xpath("//div[@class='m-v-sm info']/span/text()")[3]
        item['desc'] = d_html.xpath("//div[@class='drama']/p/text()")[0].replace('\n', '').strip()
    except Exception as e:
        item['error'] = str(e)

    return item



# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r



# 获得所有的详情页 url
def get_url():
    url_list = []

    for i in range(1,101):
        detail_url = url.format(i)
        url_list.append(detail_url)

    return url_list



def work(t):
    url,coll = t
    item = parse_detail(url)

    r = save_mongo(item, coll)

    print(r)


def run(coll):
    url_list = get_url()

    pool = ThreadPoolExecutor(max_workers=8)

    pool.map(work, [(url,coll) for url in url_list])




if __name__ == '__main__':
    run('ssr4')
