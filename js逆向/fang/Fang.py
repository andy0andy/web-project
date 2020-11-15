import requests
from fake_useragent import UserAgent
import json
import execjs
import os



ua = UserAgent()


class Fang(object):


    def _pwd(self, pwd):
        
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "RSA.js"), 'r', encoding='utf-8') as f:
            RSA = execjs.compile(f.read())
        
        res = RSA.call("getPwd",  pwd)

        return res


    def login(self, username, pwd):

        url = "https://passport.fang.com/login.api"

        headers = {
            "User-Agent": ua.random,
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "316",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Host": "passport.fang.com",
            "Origin": "https://passport.fang.com",
            "Referer": "https://passport.fang.com/?backurl=https://esf.fang.com/esfcities.aspx",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }

        form_data = {
            "uid": username,
            "pwd": self._pwd(pwd),
            "Service": "soufun-passport-web",
            "AutoLogin": "0"
        }

        response = requests.post(url, headers=headers, data=form_data)

        print(response.json())


        r = requests.get("https://esf.fang.com/newsecond/include/DefaultUserLoginNew.aspx?method=init", headers=headers)
        print(r.cookies.items())


if __name__ == "__main__":
    fang = Fang()

    fang.login('18879204457', '1472942893wjh')





