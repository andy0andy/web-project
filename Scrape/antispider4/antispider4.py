import requests
from lxml import etree
import pymongo
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent



'''
对接字体文件反爬，显示的内容并不在 HTML 内，而是隐藏在字体文件，设置了文字映射表，适合用作字体反爬练习。
'''

# 查看css找到对应的数字
FONT_MAP = {
    "icon-981": ".",

    "icon-272": "0",

    "icon-643": "1",

    "icon-180": "2",

    "icon-437": "3",

    "icon-378": "4",

    "icon-504": "5",

    "icon-203": "6",

    "icon-102": "7",

    "icon-281": "8",

    "icon-789": "9",
}

url = "https://antispider4.scrape.center/api/movie/{}/"

ua = UserAgent()


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

    headers = {
        'User-Agent': ua.random,
    }

    r = requests.get(url,headers=headers)

    if r.status_code != 200:
        return None

    # data = r.text
    data = r.json()

    return data



# 返回字典类型数据
def parse_detail(data):
    html = etree.HTML(data, parser=etree.HTMLParser())

    item = {}

    item['title'] = html.xpath("//h2[@class='m-b-sm']/text()")[0].replace('\n','').replace(' ','')

    score = html.xpath("//p[@class='score m-t-md m-b-n-sm']//i/@class")
    score = [s.split(' ')[1] for s in score]

    item['score'] = ''.join([FONT_MAP[s] for s in score])

    item['tags'] = html.xpath("//div[@class='categories']//span/text()")
    item['addr'] = html.xpath("//div[@class='m-v-sm info'][1]/span[1]/text()")[0].replace('\n','').replace(' ','')
    item['time'] = html.xpath("//div[@class='m-v-sm info'][1]/span[3]/text()")[0].replace('\n','').replace(' ','')
    item['show'] = html.xpath("//div[@class='m-v-sm info'][2]/span[1]/text()")[0].replace('\n','').replace(' ','')
    item['cover'] = html.xpath("//div[@class='drama']/p/text()")[0].replace('\n','').replace(' ','')

    return item



def work(t):
    url,coll = t

    data = get_data(url)
    print(data)

    # item = parse_detail(data)
    # print(item)
    item = data

    r = save_mongo(item,coll)
    print(r)


def run(coll):
    pool = ThreadPoolExecutor(max_workers=8)

    pool.map(work,[(url,coll) for url in get_url()])




if __name__ == '__main__':

    run("antispider4")




