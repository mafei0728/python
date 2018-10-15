#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,struct
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect(('127.0.0.1',10010))
while True:
    mes = input('ssh-->')
    if not mes:
        continue
    if mes == 'quit':
        break
    s1.send(mes.encode('utf8'))
    #先收4个字节的报头
    data_size = s1.recv(4)
    data_size = struct.unpack('i',data_size)[0]
    recv_size = 0
    recv_data = b''
    #确定收到的长度的数据才停止收包
    while recv_size < data_size:
        data = s1.recv(1024)
        recv_size += len(data)
        recv_data += data
    print(recv_data.decode('gbk'))
s1.close()