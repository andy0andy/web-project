import requests
from fake_useragent import UserAgent
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import pymongo


'''
对接 JWT 模拟登录方式，适合用作 JWT 模拟登录练习。
'''

ua = UserAgent()

# 登入获取 jwt token
def login(url,data):

    js_data = requests.post(url,data).json()

    return js_data['token']


# 获取单个页面的json 数据
def one_page(url,tk):
    headers = {
        'User-Agent': ua.random,
        'authorization': 'jwt ' + tk
    }

    r = requests.get(url,headers=headers)

    return r.json()




# 通过列表获取没详情页的id
def pages(page_url,tk):

    for i in range(1,513):
        url = page_url.format((i - 1) * 18)

        js_data = one_page(url,tk)

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

        url, tk, col = q.get()

        # 详情页，获取单个页面数据
        detail_data = one_page(url,tk)

        # 保存数据，保存至mongo中
        r = save_mongo(detail_data,col)

        print(url,r,'ok')



def run(col):
    login_url = "https://login3.scrape.center/api/login"
    data = {
        'username': 'admin',
        'password': 'admin'
    }
    page_url = "https://login3.scrape.center/api/book/?limit=18&offset={}"
    detail_url = "https://login3.scrape.center/api/book/{}/"

    pool = ThreadPoolExecutor(max_workers = 12)
    q = Queue()

    # 登录，获取jwt tkoen
    tk = login(login_url,data)
    print('jwt token：\n%s' % tk)

    # 列表页，获取所有页
    for ids in pages(page_url,tk):

        for id in ids:
            q.put([detail_url.format(id),tk,col])


    # 详情页，获取单个页面数据
    # 保存数据，保存至mongo中
    pool.map(work,[q for i in range(12)])





if __name__ == '__main__':
    run('login3')




