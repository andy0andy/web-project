# -- coding: utf-8 --

import aiowebsocket
from aiowebsocket.converses import AioWebSocket
import asyncio



'''
WebSocket 单人聊天室，适合做 WebSocket 抓包分析。
'''



async def run(uri,uh):

    async with AioWebSocket(uri, union_header=uh) as aws:
        mp = aws.manipulator    # manipulator:操纵者


        send_msg = f"你好！！！"

        await mp.send(send_msg)
        print(send_msg)

        recv_msg = await mp.receive()

        print(recv_msg)


if __name__ == '__main__':

    uri = "wss://websocket1.scrape.center/websocket"

    union_header = {
        "Connection" : "Upgrade",
        "Cookie" : "UM_distinctid=1751ba96d733de-05fcb4d876a2a9-3323767-100200-1751ba96d746db",
        "Host" : "websocket1.scrape.center",
        "Origin" : "https://websocket1.scrape.center",
        "Pragma" : "no-cache",
        "Sec-WebSocket-Extensions" : "permessage-deflate; client_max_window_bits",
        "Sec-WebSocket-Key" : "5wP0pyyNAt6B+eQt5Mx+CQ==",
        "Sec-WebSocket-Version" : "13",
        "Upgrade" : "websocket",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    }


    loop = asyncio.get_event_loop()

    task = asyncio.ensure_future(run(uri,union_header))

    loop.run_until_complete(task)


