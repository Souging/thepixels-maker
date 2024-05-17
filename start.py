import json
import random
import time

from curl_cffi import requests

proxy = {'http': 'http://127.0.0.1:10809',
         'https': "http://127.0.0.1:10809"}
def login():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "content-length": "0",
        "dnt": "1",
        "origin": "https://the-pixels-game.fireheadz.games",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://the-pixels-game.fireheadz.games/",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }
    url = ""
    params = {
        "_p": "web"
    }
    response = requests.put(url, headers=headers, params=params, impersonate="chrome110")
    return response.json()['accessToken']

def set_pixels(drawKey):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": f"Bearer {ck}",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://the-pixels-game.fireheadz.games",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://the-pixels-game.fireheadz.games/",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    }
    url = "https://thepixels.fireheadz.games/api/canvas/set-pixels"
    data = {
        "drawKey": drawKey,
        "targetId": "b920c802-33e4-4c60-b5e3-6f5fb3bc12fc",#社区创建的目标图片ID
        "pixels": [
            {"id": 673077, "color": random.randint(4270000000, 4284314780)},
            {"id": 644411, "color": random.randint(4270000000,4284314780) },
            {"id": 506586, "color": random.randint(4270000000, 4284314780)}

        ]
    }
    #388277ce-c7d3-4588-b9f1-6f6faa5e64c4
    # {"id": 632136,"color": 4284314780},
    # 673077
    #random.randint() 513536 ,632997  500000,690000
    data = json.dumps(data, separators=(',', ':'))
    response = requests.put(url, headers=headers, data=data, proxies=proxy)
    print(response.text)
    return response.json()['lastDrawId']

def drawxy(id):
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh-Hans;q=0.9",
        "authorization": f"Bearer {ck}",
        "cache-control": "no-cache",
        "content-type": "application/json",
        "dnt": "1",
        "origin": "https://the-pixels-game.fireheadz.games",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://the-pixels-game.fireheadz.games/",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    }
    url = f"https://thepixels.fireheadz.games/api/draw/{id}?pixelId=-1"
    response = requests.get(url, headers=headers, proxies=proxy)
    str = response.json()
    if str['pixel']['mintData'] == None:
        print(
            f"id:{str['id']},color:{str['color']},x:{str['target']['x']},y:{str['target']['y']},未mint")

    else:
        print(
            f"id:{str['id']},color:{str['color']},x:{str['target']['x']},y:{str['target']['y']},收益:{str['pixel']['mintData']['profit']},日收益:{str['pixel']['mintData']['dailyProfit']}")


def draw():
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "zh-CN,zh;q=0.9",
        "authorization": f"Bearer {ck}",
        "cache-control": "no-cache",
        "content-length": "0",
        "dnt": "1",
        "origin": "https://the-pixels-game.fireheadz.games",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://the-pixels-game.fireheadz.games/",
        "user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    }
    url = "https://thepixels.fireheadz.games/api/canvas/draw-request"
    response = requests.put(url, headers=headers, proxies=proxy)

    #print(response.text)
    return response.json()['drawKey']

if __name__ == '__main__':
    #ck = login()
    #ck是你的token 抓包获取
    ck = "eyJhbGciOiJIUzI1NiIsIn"
    while True:
        try:
            drawKey = draw()
            drawids = set_pixels(drawKey)
            drawxy(drawids)
        except:
            pass
        time.sleep(2.5)
