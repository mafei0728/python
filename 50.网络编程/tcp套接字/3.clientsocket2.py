#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#客服端直接请求
s1.connect(('127.0.0.1',10010))
#客服端发消息(记住是bytes)
while True:
    mes = input('----->')
    if not mes:   # 禁止发空包
        continue
    if mes == 'quit': # 退出
        break
    s1.send(mes.encode('utf8'))
    #客服端收消息
    data = s1.recv(1024)
    print(data.decode('utf8'))
    if data.decode("utf8") == 'close':
        break
s1.close()