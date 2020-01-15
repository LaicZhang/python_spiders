import requests
from lxml import etree
import csv
import re
import pymysql
import random
import time
from fake_useragent import UserAgent


csvFile = open('book.csv','w',encoding='utf-8',newline='')
csv_writer = csv.writer(csvFile)

conn = pymysql.connect('127.0.0.1', user='root', password='', db='book')
print(conn)
print(type(conn))

cursor = conn.cursor()
print(cursor)


def getFatherIntfo():
    x = requests.get("http://www.ireadweek.com/")
    html = etree.HTML(x.text)
    # print(html)
    
    print(html.xpath('//ul[@class="hanghang-list"]/a/li/div[@class="hanghang-list-name"]/text()'))
    NewestBook = html.xpath('/html/body/div/div/ul/a[3]/li/div[1]/text()')
    NewestBookLink = html.xpath('/html/body/div/div/ul/a[3]/@href')
    print('最新的书是'+ str(NewestBook) +'，它的地址是'+ str(NewestBookLink))
    NewestBookId = re.sub("\D", "", str(NewestBookLink))
    return NewestBookId


def avoid():
    ua = UserAgent()
    headers = {'User-Agent':ua.random}

    sleepTime = random.randint(0,10)
    time.sleep(sleepTime)




def getChildInfo():
    url1 = 'http://ireadweek.com/sdfesfwsf.php?m=article&a=index&id='
    avoid()

    for id in range(14, eval(getFatherIntfo())):
        url2 = url1 + str(id)
        x = requests.get(url2)
        html = etree.HTML(x.text)
        # print(html)

        print(id)# id

        bookPic = html.xpath('/html/body/div[1]/div/div[1]/div[2]/div[1]/img/@src')#封面
        bookPic = ''.join(bookPic)
        print(bookPic)

        bookName = html.xpath('//html/body/div/div/div[1]/div[2]/div[2]/p[1]/text()')# 书名
        bookName = ''.join(bookName)
        print(bookName)
        
        Author = html.xpath('//html/body/div/div/div[1]/div[2]/div[2]/p[2]/text()')# 作者
        Author = ''.join(Author)
        print(Author)

        classification = html.xpath('//html/body/div/div/div[1]/div[2]/div[2]/p[3]/text()')# 分类
        classification = ''.join(classification)
        print(classification)

        score = html.xpath('//html/body/div/div/div[1]/div[2]/div[2]/p[4]/text()')# 豆瓣评分
        score = ''.join(score)
        print(score)

        Introduction = html.xpath('//html/body/div/div/div[1]/div[2]/div[2]/p[6]/text()')# 简介
        Introduction = ''.join(Introduction)
        print(Introduction)

        Link = html.xpath('/html/body/div/div/div[1]/div[3]/div[1]/a/@href')# 下载链接
        Link = ''.join(Link)
        print(Link)

        csv_writer.writerow([id, bookPic, bookName, Author, classification, score, Introduction, Link])

        insertSql =  "insert into book values(%s,%s,%s,%s,%s,%s,%s,%s)" 
        #+ id +","+ bookPic + "," + bookName+","+Author+","+classification+","+score+","+Introduction+","+Link+ ")"
        values = (id, bookPic, bookName, Author, classification, str(score), Introduction, Link)

        cursor.execute(insertSql,values)

        conn.commit()



def CreateTable():
    cursor.execute("drop table if exists book")

    CreateTableSql = """CREATE TABLE book (
        id int(10) NOT NULL PRIMARY KEY auto_increment,
        bookPic varchar(255),
        bookName varchar(50),
        author varchar(50),
        classification varchar(50),
        score varchar(50),
        introduction text(255),
        link varchar(255)
        );"""

    cursor.execute(CreateTableSql)
    
    

if __name__ == "__main__":
    CreateTable()
    getChildInfo()
    csvFile.close()
    cursor.close()
    conn.close()
