# 遍历阿里云的国内IP，找到可以解析自己的IP上去而不影响他人使用的IP。


import requests
import threading

def get_title(ip):
	try:
		res = requests.get("http://"+ip,timeout=3)
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
		ip = f"39.100.{m}.{i}"
		t=threading.Thread(target=get_title,args=(ip,))
		t.start()
