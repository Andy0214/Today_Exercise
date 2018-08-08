#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/8/8

import requests
import xlrd
import xlwt
import json


def Get_Excel_data(file):
    file = './ip.xlsx'
    re1 = xlrd.open_workbook(file)

    outwb = xlwt.Workbook()
    outws = outwb.add_sheet("new")

    # 读取第一个sheet
    ws = re1.sheet_by_index(0)
    rows = ws.nrows   #获取行数
    outws.write(0, 0, u'IP')
    outws.write(0, 1, u'国家')
    outws.write(0, 2, u'城市')
    outws.write(0, 3, u'运营商')

    for i in range(0, rows):
        IP = str(ws.cell_value(i, 0))
        print(IP)
        url = 'http://ip.taobao.com/service/getIpInfo.php?ip=%s' % (IP)

        req = requests.get(url)
        js = json.loads(req.text)
        # print(type(js))
        outws.write(i + 1, 0, IP)
        try:
            outws.write(i + 1, 1, js['data']['country'])
            outws.write(i + 1, 2, js['data']['city'])
            outws.write(i + 1, 3, js['data']['isp'])

            outwb.save(r'new_ip.xls')
        except:
            print("none")


def main():
    file = './ip.xlsx'
    Get_Excel_data(file)


if __name__ == '__main__':
    main()