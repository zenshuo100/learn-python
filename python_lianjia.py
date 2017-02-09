# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 14:19:29 2017

@author: forever
"""
from bs4 import BeautifulSoup
import requests
import time
#proxy = {'http':'http://120.27.110.37'}
#,proxies = proxy
csvfile = open("lianjia.csv","a")
url = "http://bj.lianjia.com/ershoufang/pg"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.98 Safari/537.36 Vivaldi/1.6.689.40'}
for k in range(1,2):

    req = requests.get( "http://bj.lianjia.com/ershoufang/pg"+str(k),headers = headers,timeout=5)
    req.encoding = ('utf8')
    csvfile = open("lianjia.csv","a")
    soup = BeautifulSoup(req.text, "html.parser")
    for tag in soup.find_all("div","info clear"):
        tag_addr = tag.find("div", "address")
        print(tag_addr.text)
        tag_total_price = tag.find("div","totalPrice")
        tag_unit_price = tag.find("div","unitPrice")
        addr = tag_addr.text.replace("|",",")
        tag_addr1 = addr.split(',')

        if (len(tag_addr1) == 5):
            tag_addr1.append('无电梯')          
        csvfile.write(','.join(tag_addr1) +" , " + tag_total_price.text + " , "+ tag_unit_price.text+"\n")
csvfile.close()
        