import requests
from lxml import etree
import pymongo
from fake_useragent import UserAgent
from loguru import logger


'''
限制单个 IP 访问频率 5 分钟最多 10 次，如果过多则会封禁 IP 10 分钟。
'''


# 代理ip
def proxies():

    url = "http://1472942893.v4.dailiyun.com/query.txt"

    params = {
        "key": "NP42BC9688",
        "word": "上海",
        "count": 100,
        "rand": True,
        "detail": True,
    }

    r = requests.get(url, params)

    # 代理服务器地址,外网ip，位置描述，入库时间（unix）,过期时间(unix)
    px = r.text

    if px:
        px = px.replace("\r\n", '').split(',')

        res = {
            'code': 1,
            "proxy": {'http': f'http://{px[0]}', 'https': f'https://{px[0]}'},
            "time": (int(px[-1]) - int(px[-2])) // 60
        }
    else:
        res = {'code':-1}


    return res


# 提取数据
def parse_data(text):
    html = etree.HTML(text,parser=etree.HTMLParser())


    title = html.xpath("//h2[@class='m-b-sm']/text()")

    print(title)


# 获取所有页
def all_page():
    ua = UserAgent()

    url = "https://antispider5.scrape.center/detail/{}"

    for i in range(1, 101):
        headers = {
            "User-Agent": ua.random
        }

        px = proxies()
        if px['code'] == 1:
            proxy = px['proxy']
        else:
            logger.info("No proxies!")
            continue

        try:
            page = requests.get(url, headers=headers, proxies=proxy).text
            yield page
        except Exception as e:
            logger.error(f"page: {i}", e)
            yield None



def run():

    for page in all_page():
        if not page:
            continue

        data = parse_data(page)



if __name__ == '__main__':

    px = proxies()
    print(px)

    run()

