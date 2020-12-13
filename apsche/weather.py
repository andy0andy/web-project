import requests
import time
from faker import Faker
import json
from loguru import logger
import re
import time

# 发送邮件
import smtplib
from email.header import Header
from email.mime.text import MIMEText


fake = Faker()



class Weather(object):

    def city(self):

        url = "https://j.i8tq.com/weather2020/search/city.js"

        headers = {
            "User-Agent": fake.user_agent(),
            "Referer": "http://www.weather.com.cn/"
        }


        resq = requests.get(url, headers=headers)

        data = resq.text
        data = eval(data.lstrip("var city_data = "))

        try:
            json.dump(data, open("city.json",'w'), ensure_ascii=False)
            logger.info(f"city.js download success")

            return data
        except Exception as e:
            logger.debug(f"{self.__class__.__name__} - {str(e)}")
            return
    
    def queryAreaid(self, addr="广东,深圳,深圳"):
        try:
            if addr.count(",") != 2:
                logger.debug("请正确输入查询天气地址...")

            # city = json.load(open("city.json",'r'))
            city = self.city()

            addr_list = addr.split(',')
            

            while addr_list:
                a = addr_list.pop(0)
                city = city[a]
            
            return city['AREAID']
        except Exception as e:
            raise Exception(f"{self.__class__} - {str(e)}")


    def weatherInfo(self, addr="广东,深圳,深圳"):

        url = f"http://d1.weather.com.cn/weather_index/{self.queryAreaid(addr)}.html"

        headers = {
            "User-Agent": fake.user_agent(),
            "Referer": "http://www.weather.com.cn/"
        }

        params = {
            "_": str(int(time.time()*1000))
        }

        resq = requests.get(url, headers=headers, params=params)
        resq.encoding = resq.apparent_encoding
        
        data = re.findall("{(.+?)};", resq.text)
        d_1 = eval("{"+data[2]+"}")
        d_2 = eval("{"+data[3]+"}")["zs"]
        tips = []
        t = ""
        for i,l in enumerate([v for k,v in d_2.items()][1:]):
            t += "，" + l.strip()

            if (i+1) % 3 == 0:
                tips.append(t.lstrip("，")) 
                t = ""
        

        info = {
            "content": {
                "cityname": d_1["cityname"],  # 城市
                "temp": d_1["temp"],  # 温度
                "wind": d_1["WD"] + "-" + d_1["WS"],    # 风向风力
                "weather": d_1["weather"],   # 天气
                "sd": d_1["sd"],  # 相对湿度
                "aqi_pm25": d_1["aqi_pm25"],  # pm2.5
            } ,
            "tips": tips
        }

        return info




def sendEmail(receUser, w = ""):

    try:
        # 实例化
        smtp = smtplib.SMTP()
        # 连接qq邮箱
        smtp.connect("smtp.qq.com", 25)
        smtp.login('1472942893', 'shotjegszycaidcf')

        if w == "":
            msg = w
        else:
            msg = '''
            城市/天气：{: ^20}{: ^20} \n
            温度/风向：{: ^20}{: ^20} \n
            相对湿度/pm2.5：{: ^20}{: ^20} \n
            '''.format(w['content']['cityname'], w['content']['weather'], w['content']['temp'], w['content']['wind'], w['content']['sd'], w['content']['aqi_pm25'])
            
            for t in w['tips']:
                msg += "\n{: <100}\n".format(t)

        # print(msg)

        msg = MIMEText(msg, 'plain', 'utf-8')   # 邮件
        msg['From'] = Header("Andy", 'utf-8')   # 发送者
        msg['To'] = Header("Dear you", 'utf-8') # 接收者
        msg['Subject'] = Header(f"{time.asctime()} 天气预报")   # 邮件标题

        # 发送
        smtp.sendmail("1472942893@qq.com", receUser,msg.as_string())

        smtp.quit()

        logger.info("发送邮件成功")
    except Exception as e:
        logger.debug(f"发送邮件失败 - {str(e)}")






if __name__ == "__main__":
    weather = Weather()

    
    info = weather.weatherInfo()
    # print(info)

    sendEmail(['1472942893@qq.com'], info)

