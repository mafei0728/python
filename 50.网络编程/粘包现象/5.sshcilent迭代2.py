#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,struct,json
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s1.connect(('127.0.0.1',10010))
while True:
    mes = input('ssh-->')
    if not mes:
        continue
    if mes == 'quit':
        break
    s1.send(mes.encode('utf8'))
    '''先收4个字节的报头字点长度'''
    head_pack_four = s1.recv(4)
    head_dick_len = struct.unpack('i',head_pack_four)[0]
    '''在收报头字典'''
    head_dick_byte = s1.recv(head_dick_len)
    head_dick_json = head_dick_byte.decode('utf8')
    head_dick = json.loads(head_dick_json)
    '''通过报头字典得到数据长度'''
    data_size = head_dick['data_size']
    recv_size = 0
    recv_data = b''
    '''确定收到的长度的数据才停止收包'''
    while recv_size < data_size:
        data = s1.recv(1024)
        recv_size += len(data)
        recv_data += data
    print(recv_data.decode('gbk'))
s1.close()