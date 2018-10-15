#!/usr/bin/env python
# -*- coding:utf-8 -*-
import subprocess,socket,struct,json
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
    #print(s1.getpeername())
    flag = False
    while not flag:
        print('等待客服端...')
        conn,addr = s1.accept()
        print("客服端", addr)
        print('客服端以连接...')
        while not flag:
            '''客服端断开,服务端继续处理'''
            try:
                data = conn.recv(1024)
                data = data.decode('utf8')
                data = w_cmd(data)
                '''先确定数据的长度'''
                data_size = len(data[0])+len(data[1])
                '''封装到报头字典'''
                head_dick ={'data_size':data_size}
                '''打包成json格式并编码'''
                head_dick_json = json.dumps(head_dick)
                head_dick_byte = head_dick_json.encode('utf8')
                '''打包字典长度固定四个字节'''
                head_pack_four = struct.pack('i',len(head_dick_byte))
                '''先发送固定4字节,在发送报头字典,最后发送数据'''
                conn.send(head_pack_four)
                conn.send(head_dick_byte)
                conn.send(data[0])
                conn.send(data[1])
            except ConnectionResetError:
                break
    conn.close()
    s1.close()
ssh_m()