from gettext import find
import requests
import schedule
import time
from datetime import datetime
 
def run():
    res = requests.get('https://cherbim.ml/')
    print(datetime.now(), res)
    r = res.text
    if r.find('xxx')!=-1:
        requests.get('https://api2.pushdeer.com/message/push?pushkey=xxxxxx&text=服务器有货了')

schedule.every(90).seconds.do(run)    # 每隔1分钟执行一次
 
if __name__ == '__main__':
    while True:
        schedule.run_pending()
