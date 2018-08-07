#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/8/7

import requests, bs4

#data-spm-anchor-id="0.0.0.i2.105b1011adF71t"

'''
<span class="sip">211.94.162.7</span>
'''
ip = '211.94.162.6'
res = requests.get('http://ip.taobao.com/ipSearch.html?ipAddr=ip')
# logging.debug(res.status_code == requests.codes.ok)#检测网页是否下载成功

try:
    res.raise_for_status()#检测网页是否下载成功
except Exception as exc:
    print('There was a problem: %s' % (exc))


noStarchSoup = bs4.BeautifulSoup(res.text)

print(noStarchSoup)
print(type(noStarchSoup))

playFile = open('RomeoAndJuliet.txt', 'wb')
playFile.write(noStarchSoup.get_text)
playFile.close()

# elems = noStarchSoup.select('#author')
