#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 基于网络的tcp协议
s1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #重用,当端口存在时候,在启动服务避免冲突报错
s1.bind(('127.0.0.1',10010)) # 绑定服务端的地址和端口
s1.listen(5)  # 激活服务端,服务端的半连接池.缓存客服端的数量,通过变量传参
print('server start') # 打印这个说明服务端正常运行
# 等待客服端 连接地址,和端口
flag = False
while not flag:
    print('等待客服端...')
    info = s1.accept()
    conn,addr = info
    print(info)
    print("客服端",addr)
    print('客服端以连接...')  # 打印这个说明服务端接收到了客服端的数据
    #收消息,循环沟通
    while not flag:
        try:   # windows在客服端单方面终端会报错,我们要做异常判断
            data = conn.recv(1024) # 从自己的缓存里面最大收1024个字节,其实默认就是1024
            if not data:break # linux不会报错,会卡死,这里应对linux系统,最后发现windows正常close也会发空包,所以这里都加上去
            data = data.decode('utf8')
            print(data)
            data = data.upper()
            data = data.encode('utf8')
            conn.send(data)
        except ConnectionResetError:
            break
#关闭连接
conn.close()
#服务端关闭
s1.close()