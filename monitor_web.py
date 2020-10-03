# 监控网站，并在网站可以访问时通过server酱通知我。

import requests
import time


KEY = ""
api = "https://sc.ftqq.com/{KEY}.send".format(KEY = KEY)
monitorWeb = "https://baidu.com/" #"http://kzp.mof.gov.cn/"
title = u"通知"
content = "qwe"
data = {
   "text":title,
   "desp":content
   }

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

while(True):
    if (requests.get(monitorWeb).status_code == 200):
        req = requests.post(api,data = data,headers = headers)
        if(req.status_code == 200):
            break
    else:
        time.sleep(30)
        print("Request failed")
