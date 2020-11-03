from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytesseract
from PIL import Image



'''
对接普通图像验证码，干扰较少，适合 OCR 识别。
'''


url = "https://captcha7.scrape.center/"

username = password = 'admin'

# 二值化
def threshold(img,t=70):
    '''
    获取灰度转二值的映射table
    0表示黑色,1表示白色
    '''
    table = []
    for i in range(256):
        if i < t:
            table.append(0)
        else:
            table.append(1)

    img = img.point(table,'1')
    return img


def verify_code(path):
    img = Image.open(path)

    # 转灰度图
    img = img.convert('L')

    # 二值化
    img = threshold(img,100)


    text = pytesseract.image_to_string(img)

    text = text.replace(' ','')

    return text




def run():
    driver = webdriver.Chrome()

    driver.get(url)
    driver.maximize_window()

    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[1]/div/div/input').send_keys(username)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[2]/div/div/input').send_keys(password)


    captcha = driver.find_element(By.ID,'captcha')

    # 验证码在屏幕位置
    location = captcha.location
    print("验证码位置：%s" % str(location))

    # 验证码大小
    size = captcha.size
    print("验证码大小：%s" % str(size))

    # 截屏
    driver.save_screenshot('screen.png')

    # 截取验证码图片
    img = Image.open('screen.png')

    box = (location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height'])
    yzm = img.crop(box)
    yzm.save('yzm.png')


    code = verify_code('yzm.png')
    print("验证码：%s" % code)

    driver.find_element(By.XPATH, '//*[@id="app"]/div[2]/div/div/div/div/div/form/div[3]/div/div/div[1]/div/input').send_keys(code)
    driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div/div/div/div/div/form/div[4]/div/button').click()


    try:
        WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'text-center')))
        succ = driver.find_element(By.CLASS_NAME,'text-center').text
        print(succ)
    except:
        print("验证错误，请重试...")






if __name__ == '__main__':
    run()
    input()

    # code = verify_code('yzm.png')
    # print("验证码：%s" % code)
