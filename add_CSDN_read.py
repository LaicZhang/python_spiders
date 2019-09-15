# -*- coding:utf-8 -*-
# 利用爬虫刷CSDN博客阅读数

import requests
from bs4 import BeautifulSoup
import time

# 解析源码
def GetHtmlText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''

# 查找博文地址并进行一次点击
def Find_Click(soup):
    Divs = soup.find_all('div', {'class': 'article-item-box csdn-tracking-statistics'})
    for Div in Divs:
        ClickUrl = Div.find('h4').find('a')['href']
        # 点一下
        Click = requests.get(ClickUrl, timeout = 30)

def main():
    # 博文页数
    # Pages = int(input('Please enter the number of blog pages:'))
    Pages = 13 # 此刻我的blog有13页
    for Page in range(1, Pages + 1):
        print('Page=', Page)
        # 博客地址，这里是我的CSDN博客地址
        url = 'https://blog.csdn.net/qq_44621510/article/list/' + str(Page)
        html = GetHtmlText(url)
        soup = BeautifulSoup(html, 'html.parser')
        Find_Click(soup)

if __name__ == '__main__':
    while 1:
        main()
        time.sleep(30)
