#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess,socket,struct
def w_cmd(cmd):
    res = subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    res1 = res.stdout.read()
    res2 = res.stderr.read()
    return res1,res2
def ssh_m():
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s1.bind(('127.0.0.1', 10010))
    s1.listen(5)
    print('server start')
    flag = False
    while not flag:
        print('等待客服端...')
        conn,addr = s1.accept()
        print("客服端", addr)
        print('客服端以连接...')
        while not flag:
            try:
                data = conn.recv(1024)
                data = data.decode('utf8')
                data = w_cmd(data)
                #封装前4个字节的数据长度
                data_size = len(data[0])+len(data[1])
                conn.send(struct.pack('i',data_size))
                conn.send(data[0])
                conn.send(data[1])
            except ConnectionResetError:
                break
    conn.close()
    s1.close()
ssh_m()