#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/8/7

import webbrowser, sys, logging, pyperclip, requests

logging.disable(logging.CRITICAL)
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')

# if len(sys.argv)>1 :
#     #TODO：从命令行获取地址
#     city = ' '.join(sys.argv[1:])
#     logging.debug(city)
# else:
#     #TODO：从剪贴板获取地址
#     city = pyperclip.paste()
# webbrowser.open('http://www.15tianqi.com/' + city) #webbrowser 模块的 open()函数可以启动一个新浏览器


'''
用 requests 模块从 Web 下载文件
requests.get()函数下载一个网页
'''
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# logging.debug(res.status_code == requests.codes.ok)#检测网页是否下载成功

try:
    res.raise_for_status()#检测网页是否下载成功
except Exception as exc:
    print('There was a problem: %s' % (exc))

logging.debug(type(res))
logging.debug(len(res.text))
logging.debug(res.text[:100])

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content():
    playFile.write(chunk)
playFile.close()