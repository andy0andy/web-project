from playwright import async_playwright
import asyncio
import os
import json
from PIL import Image
from loguru import logger
import time
import re


# 异常处理
def errPro(func):
    def inner(*args, **kwargs):

        try: 
            res = func(*args, **kwargs)
            return res
        except Exception as e:
            raise Exception(f"{func.__name__} - {str(e)}")
    return inner



#去除特殊字符
def isSpec(l):
    l = json.loads(l)

    comp = re.compile("[\u4e00-\u9fa5a-zA-Z\-0-9]{0,}")

    for k,v in l.items():
        words = comp.findall(v)
        words = "".join(words)

        l[k] = words
    
    return l




# 读取songs.txt
@errPro
def readSong():

    songs = os.path.join(os.path.abspath(os.path.dirname(__file__)), "songs.txt")


    with open(songs, "r", encoding='utf-8') as f:
        song_list = [isSpec(l) for l in f.readlines()]



    return song_list

# 剪切图片
@errPro
def cropPic(pic_path, box):
    img = Image.open(pic_path)
    img = img.convert("RGB")

    img = img.crop(box)

    img.save(pic_path)
    
    logger.info(f"{pic_path} ok")





@errPro
async def screenshotPic(songInfo, browser, semaphore):
    url = f"https://yoopu.me/view/{songInfo['id']}"
    pic_path = os.path.join(os.path.join(os.path.abspath(os.path.dirname(__file__)), "pus"), f"{songInfo['title']}-{songInfo['artist']}-{songInfo['type']}.png")

    async with semaphore:

        page = await browser.newPage()

        await page.goto(url)
        
        logger.info(f"{songInfo['title']} start")

        # 等待
        await page.waitForSelector("//hexi-sheet")


        # 注入js
        await page.addScriptTag(content='''
            document.getElementsByTagName("yp-slider-play")[0].style.display = "none";
            document.getElementsByClassName("fullscreen-button yoopu3-icon")[0].style.display = "none";
        ''')


        # 获得谱子对象
        pu = await page.querySelector("//hexi-sheet")

        # 获得谱子的边界框值: {左上点xy坐标和宽高} -> dict
        location = await pu.boundingBox()
        
        # 调整页面大小
        await page.setViewportSize(width=int(location['width']*1.2), height=int(location['height']*1.2))

        # 重新获取谱子的大小
        location = await pu.boundingBox()

        # 截屏
        await page.screenshot(path=pic_path)

        # 剪切图片
        box = [location["x"], location["y"], location["x"]+location["width"], location["y"]+location["height"]]
        cropPic(pic_path, box)

        await page.close()
        logger.info(f"{songInfo['title']} end")


async def main():

    async with async_playwright() as asp:

        browser = await asp.chromium.launch(headless=True)

        # 信号量，限制并发数
        semaphore = asyncio.Semaphore(6)

        song_list = readSong()

        tasks = [asyncio.ensure_future(screenshotPic(song, browser, semaphore)) for song in song_list]

        dones, pendings = await asyncio.wait(tasks)

        for t in dones:
            t.result()

        await browser.close()


if __name__ == "__main__":

    start = time.time()

    log = logger.add(os.path.join(os.path.abspath(os.path.dirname(__file__)), "yoopu.log"))

    loop = asyncio.get_event_loop()

    loop.run_until_complete(main())

    end = time.time()

    logger.info(f"共耗时：{end - start}s")











