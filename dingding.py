import time

import requests
import json

header = {
    "Host": "mryb.zjut.edu.cn",
    "Accept": "application/json, text/plain, */*",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Content-Type": "application/json;charset=utf-8",
    "Origin": "http://mryb.zjut.edu.cn",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19E258 AliApp(DingTalk/6.5.5) com.laiwang.DingTalk/23636891 Channel/201200 Pad/iPad language/zh-Hans-CN UT4Aplus/0.0.6 WK",
    "Content-Length": "607",
    "DingTalk-Flag": "1",
    "Referer": "http://mryb.zjut.edu.cn/"
}
url = 'http://mryb.zjut.edu.cn/htk/baseInfo/save'
with open('ts.json', 'r') as f:
    data = f.read()
respoense = requests.post(url, data=data, headers=header)
print(respoense.text)
time.sleep(2)