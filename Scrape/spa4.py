import requests
import pymongo
from lxml import etree
from concurrent.futures import ThreadPoolExecutor


'''
新闻网站索引，无反爬，数据通过 Ajax 加载，无页码翻页，适合 Ajax 分析和动态页面渲染抓取以及智能页面提取分析。
'''


url = "https://spa4.scrape.center/api/news/?limit=10&offset={}"


# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r



# 获得url
def get_url():
    for i in range(0,291310,10):

        detail_url = url.format(i)
        yield detail_url



# 返回json
def get_json(url):
    r = requests.get(url)

    if r.status_code != 200:
        return None

    js_data = r.json()

    return js_data


# 返回html
def get_html(url):
    r = requests.get(url)
    r.encoding = r.apparent_encoding

    if r.status_code != 200:
        return None

    html = etree.HTML(r.text,parser=etree.HTMLParser(encoding='utf-8'))

    return html




# 返回字典类型数据
def parse_detail(js_data):



    item = {}

    item['title'] = js_data['title']
    item['url'] = js_data['url']
    item['website'] = js_data['website']
    item['thumb'] = js_data['thumb']
    item['domain'] = js_data['domain']
    item['published_at'] = js_data['published_at']
    item['updated_at'] = js_data['updated_at']


    return item



def parse_content(url,domain):
    html = get_html(url)
    data = {}

    if domain == "news.163.com":
        media = html.xpath("//div[@id='epContentLeft']/div[@class='post_time_source']/a[1]/text()")
        artibody = html.xpath("string(//div[@id='epContentLeft']//div[@class='post_text'])")

        data['media'] = media
        data['artibody'] = artibody
    elif domain == "news.sina.com.cn":
        media = html.xpath("//span[@class='source']/text()")
        artibody = html.xpath("string(//div[@id='artibody'])")
        artibtm = html.xpath("//div[@id='article-bottom']/div[@class='keywords']/a/text()")

        data['media'] = media
        data['artibody'] = artibody
        data['artibtm'] = artibtm

    return data



def work(t):
    url,coll = t

    js_data = get_json(url)

    for one_data in js_data['results']:
        item = parse_detail(one_data)

        data = parse_content(item['url'],item['domain'])

        for k,v in data.items():
            item[k] = v


        # print(item)
        r = save_mongo(item,coll)
        print(r)


def run(coll):
    pool = ThreadPoolExecutor(max_workers=8)

    pool.map(work,[(url,coll) for url in get_url()])


if __name__ == '__main__':
    run('spa4')