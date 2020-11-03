import requests
from fake_useragent import UserAgent
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import pymongo


'''
对接文字偏移反爬，所见顺序并不一定和源码顺序一致，适合用作文字偏移反爬练习。
'''

ua = UserAgent()



# 获取单个页面的json 数据
def one_page(url):
    headers = {
        'User-Agent': ua.random,
    }

    r = requests.get(url,headers=headers)

    return r.json()




# 通过列表获取没详情页的id
def pages(page_url):

    for i in range(1,513):
        url = page_url.format((i - 1) * 18)

        js_data = one_page(url)

        ids = [res['id'] for res in js_data['results']]

        print(ids)
        yield ids


# 保存至mongo中
def save_mongo(item,collection):
    cli = pymongo.MongoClient("mongodb://175.24.50.215:27017/")
    db = cli['test']
    col = db[collection]

    r = col.insert_one(item)

    return r

def work(q):

    while not q.empty():

        url, col = q.get()

        # 详情页，获取单个页面数据
        detail_data = one_page(url)

        # 保存数据，保存至mongo中
        r = save_mongo(detail_data,col)

        print(url,r,'ok')



def run(col):
    page_url = "https://antispider3.scrape.center/api/book/?limit=18&offset={}"
    detail_url = "https://antispider3.scrape.center/api/book/{}/"

    pool = ThreadPoolExecutor(max_workers = 12)
    q = Queue()


    # 列表页，获取所有页
    for ids in pages(page_url):

        for id in ids:
            q.put([detail_url.format(id),col])


    # 详情页，获取单个页面数据
    # 保存数据，保存至mongo中
    pool.map(work,[q for i in range(12)])





if __name__ == '__main__':
    run('antispider3')




