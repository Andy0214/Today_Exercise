#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/8/8

import requests
import xlrd
import xlwt
import json

def read_excel():
    data_ip = []
    file = './ip.xlsx'
    re1 = xlrd.open_workbook(file)
    ws = re1.sheet_by_index(0)
    rows = ws.nrows
    for i in range(0, rows):
        IP = str(ws.cell_value(i, 0))
        # print(IP)
        data_ip.append(IP)
    return rows,data_ip


print(read_excel()[0])
data1 = read_excel()[1]
print(data1)
for i in data1:
    print(i)

