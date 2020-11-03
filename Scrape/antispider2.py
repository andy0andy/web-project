from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree
import pymongo
from fake_useragent import UserAgent


'''
对接 User-Agent 反爬，检测到常见爬虫 User-Agent 就会拒绝响应，适合用作 User-Agent 反爬练习。
'''

ua = UserAgent()



def detail_urls():
    url = "https://antispider2.scrape.center/detail/{}"

    urls = []

    for i in range(1,101):
        urls.append(url.format(i))

    return urls


def get_item(url):

    item = {}

    headers = {
        'User-Agent': ua.random
    }

    r = requests.get(url,headers=headers , timeout=60)

    html = etree.HTML(r.text,parser=etree.HTMLParser())

    item['title'] = html.xpath("//h2[@class='m-b-sm']/text()")[0].replace('\n', '').replace(' ', '')
    item['score'] = html.xpath("//p[@class='score m-t-md m-b-n-sm']/text()")[0].replace('\n', '').replace(' ', '')
    item['tags'] = html.xpath("//div[@class='categories']//span/text()")
    item['addr'] = html.xpath("//div[@class='m-v-sm info'][1]/span[1]/text()")[0].replace('\n', '').replace(' ', '')
    item['time'] = html.xpath("//div[@class='m-v-sm info'][1]/span[3]/text()")[0].replace('\n', '').replace(' ', '')
    item['show'] = html.xpath("//div[@class='m-v-sm info'][2]/span[1]/text()")[0].replace('\n', '').replace(' ', '')
    item['cover'] = html.xpath("//div[@class='drama']/p/text()")[0].replace('\n', '').replace(' ', '')


    return item


# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r

def work(q):
    while not q.empty():
        url,col = q.get()

        # 分析详情页，返回数据
        item = get_item(url)

        # 保存至mongo
        r = save_mongo(item,col)
        print(url,r,'ok')



def run(col):
    q = Queue()
    pool = ThreadPoolExecutor(max_workers=12)

    # 所有详情页url
    urls = detail_urls()
    for url in urls:
        q.put([url,col])
        # print(url)

    pool.map(work,[q for i in range(12)])


if __name__ == '__main__':
    run('antispider2')

