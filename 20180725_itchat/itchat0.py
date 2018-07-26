#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/7/25

import itchat


#接收消息
# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg['Text'])
#
# itchat.auto_login(hotReload=True)
# itchat.run()


#发送消息
# itchat.auto_login(hotReload=True)
# itchat.send(u'测试消息发送', 'filehelper')
# itchat.send_msg("hello_world")


#直接返回消息
# @itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return msg['Text']

itchat.auto_login(hotReload=True)
itchat.run()