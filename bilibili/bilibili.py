import requests
from fake_useragent import UserAgent
import re
from loguru import logger
import os
from moviepy import editor






ua = UserAgent()

class Bilibili(object):
    

    # 保存文件
    def _get_file(self, bv, mode, url, filedir):
        logger.info(f"{mode} - {bv} download...")

        if not os.path.exists(os.path.join(filedir,bv)):
            os.mkdir(os.path.join(filedir,bv))

        file = requests.get(url).content

        with open(f"{os.path.join(filedir, os.path.join(bv, f'{mode}_{bv}.mp4'))}", 'wb') as f:
            f.write(file)

        logger.info(f"{mode} - {bv} OK!!!")

        return f"{os.path.join(filedir, f'{mode}_{bv}.mp4')}"


    # 下载音视频
    def download(self, bv):
        # 获得视屏单页面 url
        url = "https://www.bilibili.com/video/{}".format(bv)

        headers = {
            'User-Agent': ua.random
        }

        txt = requests.get(url, headers=headers).text
        
        urls = re.findall('\"baseUrl\":\"http://.+?\.mcdn\.bilivideo\.cn:.+?\"', txt)
        if urls == []:
            logger.warning("请重试...")
            return
        urls = [i[11:-1] for i in urls]

        # 获得video_url
        video_url = urls[0]

        # 获得audio_url
        audio_url = urls[-1]

        # 下载视屏音频
        self._get_file(bv, 'video', video_url, os.path.join(os.getcwd(), 'download'))
        self._get_file(bv, 'audio', audio_url, os.path.join(os.getcwd(), 'download'))


    # 音频视频拼接  *
    def intact(self, video_file, audio_file):

        video = editor.VideoFileClip(video_file)
        audio = editor.VideoFileClip(audio_file)

        new_video = editor.concatenate_videoclips([video, audio])
        new_video.write_videofile("new_video.mp4", fps=24, remove_temp=False)


    # 综合搜索接口
    def search(self, q):
        url = "https://api.bilibili.com/x/web-interface/search/all/v2"
        
        params = {
            "context": "", 
            "page": "1",
            "order": "", 
            "keyword": q,
            "duration": "", 
            "tids_1": "", 
            "tids_2": "", 
            "__refresh__": True,
            "_extra": "", 
            "highlight": "1",
            "single_column": "0"
        }

        headers = {
            'User-Agent': ua.random
        }

        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        video = data['data']['result'][-1]

        return video




if __name__ == "__main__":
    bv = "BV1t7411a75K"

    bilibili = Bilibili()

    # bilibili.download(bv)

    # bilibili.intact("download/BV1t7411a75K/audio_BV1t7411a75K.mp4", "download/BV1t7411a75K/video_BV1t7411a75K.mp4")
    
    bilibili.search("女王的棋局")

    

