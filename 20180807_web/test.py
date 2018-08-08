#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/8/8

import requests , json
import bs4
import re

url = "http://news.house.qq.com/a/20170702/003985.htm"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
res = requests.get(url, headers=headers)


data = []
soup = bs4.BeautifulSoup(res.text, "html.parser")
content = soup.find(id="Cnt-Main-Article-QQ")
# print(content)

target = iter(content.find_all("p", style="TEXT-INDENT: 2em"))
print(target)


'''
迭代器是一种支持next()操作的对象。它包含一组元素，当执行next()操作时，返回其中一个元素；
'''
for each in target:
    if each.text.isnumeric():
        # print(re.search(r'\[(.+)\]', next(target).text).group())
        # print(re.search(r'\d.*', next(target).text).group())
        data.append([
            re.search(r'\[(.+)\]', next(target).text).group(),
            re.search(r'\d.*', next(target).text).group(),
            re.search(r'\d.*', next(target).text).group(),
            re.search(r'\d.*', next(target).text).group()
            ])
print(data)