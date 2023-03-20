import http.client
import json


def getLocation():
    with open('loc.json', 'r') as f:
        data = json.load(f)
    return data["result"][0]['x'], data["result"][0]['y']


def getBaiduMap():
    conn = http.client.HTTPSConnection("api.map.baidu.com")
    payload = ''
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'api.map.baidu.com',
        'Connection': 'keep-alive'
    }
    x, y = getLocation()
    x = 112.95097361124037
    y = 28.155788763711403
    url = '/geoconv/v1/?from=3&to=5&ak=cj7497UPX8E7coVn0vSvPTE7BwT5Mdky&coords=' + str(x) + ',' + str(y)
    print(url)
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    # 将data保存为json文件
    with open('mapProjectApp/static/json/data.json', 'w') as f:
        f.write(data.decode('utf-8'))
    print(data.decode("utf-8"))


# 打开一个线程定时调用getBaiduMap函数
import threading
import time

flag = True


def timer(n):
    global flag
    while flag:
        getBaiduMap()
        time.sleep(n)


def run(refresh_time: int):
    global t
    t = threading.Thread(target=timer, args=(refresh_time,))
    t.start()


# 结束线程
def stop():
    global flag
    flag = False
    t.join()


run(3)
time.sleep(5)
print('stop')
stop()
