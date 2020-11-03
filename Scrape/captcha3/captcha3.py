from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
import time
from PIL import Image
import random

import sys
import os
sys.path.append(os.path.join(os.getcwd(),'chaojiying.py'))

import chaojiying as cjy


'''
对接图文点选验证码，适合图文点选验证码分析处理。
'''


class Captcha3(object):

    url = "https://captcha3.scrape.center/"

    username = password = "admin"

    def __init__(self):


        self._driver = webdriver.Chrome()

        self._driver.get(self.url)

        self._driver.maximize_window()


    # 显示等待
    def waitError(self, ele, t=10):

        try:
            WebDriverWait(self._driver, t).until(ec.presence_of_element_located((By.XPATH,ele)))

            return True
        except:
            return False


    # 填写用户，密码
    def fill_ipt(self):

        if not self.waitError('//button'):
            print("请重试...")
            return


        self._driver.find_element(By.XPATH,"//input[@type='text' and @class='el-input__inner']").send_keys(self.username)
        self._driver.find_element(By.XPATH,"//input[@type='password' and @class='el-input__inner']").send_keys(self.password)

        time.sleep(0.1)

        self._driver.find_element(By.XPATH, "//button/span").click()



    # 验证码破解
    def verify(self):

        if not self.waitError("//img[@class='geetest_item_img']"):
            print('请重试...')
            return

        # 截取验证图片
        geetest_item_img = self._driver.find_element(By.XPATH,"//div[@class='geetest_widget']")

        s, l = geetest_item_img.size , geetest_item_img.location
        box = (l['x'], l['y'], l['x']+s['width'], l['y']+s['height'])
        print(box)  #

        screen = self._driver.save_screenshot("screen.png")

        screen_img = Image.open('screen.png')
        screen_img = screen_img.convert("RGB")

        verify_img = screen_img.crop(box)

        verify_img.save("verify.png")

        # 验证码处理
        data = cjy.verify("verify.png",'908720',9004)

        pic_str = data['pic_str']

        pic_lct = [i.split(',') for i in pic_str.split('|')]
        print(pic_lct)


        for lct in pic_lct:
            print(lct)

            ActionChains(self._driver).move_to_element_with_offset(geetest_item_img, int(lct[0]), int(lct[1])).click().perform()

            time.sleep(0.5)




        self._driver.find_element(By.XPATH,"//div[@class='geetest_commit_tip']").click()


    # 登录
    def login(self):

        self.fill_ipt()

        self.verify()


        input(">>>")





if __name__ == '__main__':

    captcha3 = Captcha3()

    captcha3.login()

    pass




