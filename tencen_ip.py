# 功能与ali_ip.py相似。

import requests
import threading

def get_title(ip):
	try:
		res = requests.get("http://"+ip, timeout=3)
		if res.status_code == 200:
			html = res.content.decode("utf-8")
			title = html.split("<title>")[1].split("</title>")[0].strip()
		else:
			print('get error')
		title = f"{ip} {title[0:20]}"
	except Exception:
		title = None
	if (title):
		print(title)

for m in range(0,10):
	for i in range(0,255):
		ip = f"49.51.{m}.{i}"
		t=threading.Thread(target=get_title,args=(ip,))
		t.start()
