#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/8/8 11:59
# @File    : 每日一句.py
# @Author  : YHKing

from __future__ import unicode_literals
import itchat
from threading import Timer
import requests

def get_news():
    #获取金山词霸每日一句（英文，翻译）
    url = "http://open.iciba.com/dsapi"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/75.0.3770.142 Safari/537.36"}
    r = requests.get(url, headers=headers)
    #print(r)
    content = r.json()['content']
    note = r.json()['note']
    #print(content, note).text
    return content, note

def send_news():
    try:
        #message1 = get_news()[0]
        #扫描二维码，登录微信
        itchat.auto_login(hotReload = True)
        #获取对应好友的备注
        my_friend = itchat.search_friends(name=u'')#单引号里填入好友备注名
        #获取对应备注名的一串数字
        MaBaopo = my_friend[0]["UserName"]
        message1 = get_news()[0]
        #翻译
        message2 = get_news()[1]

        #发送消息
        itchat.send(message1, toUserName=MaBaopo)
        itchat.send(message2, toUserName=MaBaopo)

        #每天定时发送一次（t=86400秒），一直挂着就可以了
        t = Timer(86400, send_news)
        t.start()
    except:

        itchat.send(message1, toUserName=MaBaopo)
        itchat.send(message2, toUserName=MaBaopo)


def main():
    send_news()

if __name__ == "__main__":
    main()
