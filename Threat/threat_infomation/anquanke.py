import requests
from faker import Faker
from loguru import logger
from lxml import etree
from queue import Queue
import threading

fake = Faker()


'''
安全客漏洞数据抓取
'''


class Anquanke(object):

    def __init__(self):
        self.base_url = "https://www.anquanke.com/vul"


    def oneListPage(self, page: str) -> str:
        '''
        抓取列表单页
        '''

        headers = {
            "User-Agent": fake.user_agent(),
            "Referer": "https://www.anquanke.com/vul",
            "Host": "www.anquanke.com"
        }

        params = {
            "page": page
        }

        try:
            html = requests.get(self.base_url, headers=headers, params=params).text
        except Exception as e:
            logger.debug(f"第 {page} 页抓取错误 - {str(e)}")
            html = ""

        return html


    def parseListPage(self, text: str) -> dict:
        '''
        解析列表页
        '''

        html = etree.HTML(text, parser=etree.HTMLParser())


        trs = html.xpath("//tbody/tr")

        for tr in trs:
            item = {}
            
            item["title"] = "".join(tr.xpath(".//div[@class='vul-title-item']/a/text()")).replace("\n", "").replace("\t", "")
            item['cve'] = "".join(tr.xpath("./td[@class='vul-cve-item']/a/text()"))
            item['publish'] = "".join(tr.xpath("./td[@class='vul-date-item'][position()=1]/text()")).replace("\n", "").strip()
            item['update'] = "".join(tr.xpath("./td[@class='vul-date-item'][position()=2]/text()")).replace("\n", "").strip()

            item['detail_url'] = "".join(tr.xpath(".//div[@class='vul-title-item']/a/@href"))[4:]

            yield item



    def oneDetailPage(self, detail_url: str) -> str:
        '''
        抓取详情页
        '''

        url = self.base_url + detail_url

        headers = {
            "User-Agent": fake.user_agent(),
            "Referer": "https://www.anquanke.com/vul",
            "Host": "www.anquanke.com"
        }



        try:
            html = requests.get(url, headers=headers).text
        except Exception as e:
            logger.debug(f"{detail_url} 抓取错误 - {str(e)}")
            html = ""

        return html


    def parseDetailPage(self, text: str) -> dict:
        '''
        解析详情页
        '''

        html = etree.HTML(text, parser=etree.HTMLParser())

        item = {}

        item['type'] = "".join(html.xpath("//tbody/tr[position()=1]/td[@class='vul-info-value'][position()=2]/text()"))
        item['cnnvd-id'] = "".join(html.xpath("//tbody/tr[position()=3]/td[@class='vul-info-value'][position()=2]/text()"))
        item['cubes'] = "".join(html.xpath("//tbody/tr[position()=4]/td[@class='vul-info-value'][position()=1]/span/text()"))
        item['cvss'] = "".join(html.xpath("//tbody/tr[position()=4]/td[@class='vul-info-value'][position()=2]/span/text()"))
        item["vul_from"] = "".join(html.xpath("/html/body/main/div/div/div/div[1]/div[2]/div/a/@href"))
        item["info"] = "".join(html.xpath("//div[@class='common-left-content-container article-detail'][position()=3]/div[@class='article-content']/text()")).replace("\n", "").strip()

        return item





def work(q):
    # 任务函数

    while not q.empty():

        page = q.get()


        anquanke = Anquanke()

        text = anquanke.oneListPage(page)

        if text:
            items = anquanke.parseListPage(text)

            for item in items:

                text = anquanke.oneDetailPage(item['detail_url'])

                if not text:
                    continue

                data = anquanke.parseDetailPage(text)

                data.update(item)
                data['detail_url'] = anquanke.base_url + data['detail_url']

                # 保存数据
                print(data)
        



def run():
    # 多线程

    q = Queue()

    for i in range(32544):
        q.put(str(i))


    t_list = []

    for i in range(12):
        t = threading.Thread(target=work, args=(q,))
        t.start()
        t_list.append(t)


    for t in t_list:
        t.join()




if __name__ == "__main__":
    
    run()



    ...




