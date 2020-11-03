from selenium import webdriver
from selenium.webdriver.common.by import By
# 显示等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
from PIL import Image
import time
import random


'''
对接滑动拼图验证码，适合滑动拼图验证码分析处理。
'''

url = "https://captcha1.scrape.center/"

username = password = 'admin'


# base64转png
def base64topng(b64,name):

    with open(name,'wb') as f:
        f.write(base64.b64decode(b64))

    print(name,'下载完成')

# 找到 缺失积木 与 左边缘的距离
def get_x(pic1,pic2):
    bg = Image.open(pic1)
    bg = bg.convert('RGB')
    fullbg = Image.open(pic2)
    fullbg = fullbg.convert('RGB')
    bgx,bgy = bg.size

    max_v = [0,0,0]

    for i in range(bgx):
        for j in range(bgy):
            bg_v = bg.getpixel((i,j))
            fullbg_v = fullbg.getpixel((i,j))

            # print(i,j)
            # print(bg_v,fullbg_v)
            if bg_v != fullbg_v and all([(abs(bg_v[i] - fullbg_v[i]) > 100) for i in range(3)]):
                return i - 5

            # 查看像素值最大相差多少
    #         if abs(bg_v[0] - fullbg_v[0]) > max_v[0]:
    #             max_v[0] = abs(bg_v[0] - fullbg_v[0])
    #         elif abs(bg_v[1] - fullbg_v[1]) > max_v[1]:
    #             max_v[1] = abs(bg_v[1] - fullbg_v[1])
    #         elif abs(bg_v[2] - fullbg_v[2]) > max_v[2]:
    #             max_v[2] = abs(bg_v[2] - fullbg_v[2])
    #
    # print(max_v)

# 变速移动滑块，先加速后减速
def get_track(distance):  # distance为传入的总距离
    # 移动轨迹
    track = []
    # 当前位移
    current = 0
    # 减速阈值
    mid = distance * 4 // 5
    # 计算间隔
    t = 0.2
    # 初速度
    v = 0

    while current < distance:
        if current < mid:
            # 加速度为2
            a = 100
        else:
            # 加速度为-3
            a = -150
        v0 = v
        # 当前速度
        v = v0 + a * t
        # 移动距离
        move = v0 * t + 1 / 2 * a * t * t
        # 当前位移
        current += move

        # 边界值，不要滑过头了
        if current > distance:
            move = distance - (current - move)
            current = distance


        # 加入轨迹
        track.append(round(move))
    return track



# 填写用户名和密码
def fill_login(driver):
    # 写入用户名，密码
    TEXT = driver.find_element_by_xpath("//input[@class='el-input__inner' and @type='text']").send_keys(username)
    PWD = driver.find_element_by_xpath("//input[@class='el-input__inner' and @type='password']").send_keys(password)

    time.sleep(0.1)

    # 点击登入
    driver.find_element_by_xpath("//button[@class='el-button el-button--primary' and @type='button']").click()


def jiyan(driver):

    try:
        geetest_panel_next = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,'geetest_slider_button')))
    except:
        print("滑块加载失败，请重试...")
        return False

    # 极验滑块
    # 难点在找到 缺失积木 与 左边缘的横轴距离
    # 图片实则为两个canvas标签，下载两个图片，对比像素值，找到 x

    # 1. 下载图片
    fullbg = driver.execute_script('return document.getElementsByClassName("geetest_canvas_fullbg geetest_fade geetest_absolute")[0].toDataURL("image/png");')
    bg = driver.execute_script('return document.getElementsByClassName("geetest_canvas_bg geetest_absolute")[0].toDataURL("image/png");')

    base64topng(fullbg.split(',')[1],'fullbg.png')
    base64topng(bg.split(',')[1],'bg.png')

    # 2. 比对图片
    x = get_x('bg.png','fullbg.png')
    print('偏移',x)

    # 3. 移动滑块，使用动作链
    actions = webdriver.ActionChains(driver)

    geetest_slider_button = driver.find_element(By.CLASS_NAME,'geetest_slider_button')

    actions.click_and_hold(geetest_slider_button)

    for t in get_track(x):
        actions.move_by_offset(t,random.randint(1,10))

    time.sleep(1)

    actions.release()

    actions.perform()

    return True




def run():
    # 加载谷歌浏览器驱动
    driver = webdriver.Chrome()

    # 全屏显示
    driver.maximize_window()

    driver.get(url)


    # 写入用户名，密码
    fill_login(driver)


    # 极验滑块
    jy = jiyan(driver)


    if not jy:
        print("滑块验证失败，请重试...")
        return

    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME,'text-center')))
    except:
        print("移动滑块失败，请重试...")
        return

    succ = driver.find_element(By.CLASS_NAME,'text-center')
    print(succ.text)





if __name__ == "__main__":
    run()



