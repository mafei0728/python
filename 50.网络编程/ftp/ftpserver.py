#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,json,struct,os,subprocess,time,sys
class S1:
    """socket"""
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = True
    coding = 'utf8'
    max_size_package = 8192
    cache_queue = 10
    server_dir = r'D:\\常用下载'
    def __init__(self,server_ip_address,server_port,bind_activate=True):
        self.server_ip_address = server_ip_address
        self.server_port = server_port
        self.bind_activate = bind_activate
        self.socket = socket.socket(self.address_family,self.socket_type)
        try:
            if self.bind_activate:
                self.socket_bind()
                self.socket_setsockopt()
                self.socket_listen()
        except Exception:
            self.socket_close()
            raise

    def socket_bind(self):
        self.socket.bind((self.server_ip_address,self.server_port))

    def socket_setsockopt(self):
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def socket_listen(self):
        self.socket.listen(self.cache_queue)

    def socket_close(self):
        self.socket.close()

    def socket_connect_request(self):
        return self.socket.accept()

    def close_request(self):
        self.conn.close()

    def run(self):
        while True:
            print("等待连接")
            self.conn,self.client_addr = self.socket_connect_request()
            print(self.client_addr)
            while True:
                try:
                    head_pack_four = self.conn.recv(4)
                    if not head_pack_four:break
                    head_dick_len = struct.unpack('i',head_pack_four)[0]
                    head_dick_byte = self.conn.recv(head_dick_len)
                    head_dick_json = head_dick_byte.decode(self.coding)
                    head_dick = json.loads(head_dick_json)
                    cmd = head_dick['cmd']
                    if hasattr(self,cmd):
                       fun = getattr(self,cmd)
                       fun(head_dick)
                    else:
                        fun = self.ssh
                        fun(cmd)
                except ConnectionResetError:
                    break
        self.close_requset(conn)
        self.socket_close()

    def put(self,head_dick):
        """客服端上传文件"""
        filepath = os.path.normpath(os.path.join(self.server_dir,head_dick["filename"]))
        if os.path.isfile(filepath):
            os.remove(filepath)
        data_size = 0
        filesize = head_dick["filesize"]
        print(filesize)
        f = open(filepath,"wb")
        while filesize > data_size:
            recv_data = self.conn.recv(self.max_size_package)
            f.write(recv_data)
            data_size += len(recv_data)
            percent=(data_size/filesize)*100
            print('%.2f%%'%percent)
        print('下载完成')
        f.close()

    def get(self,head_dick):
        """客服端下载文件"""
        filename = head_dick['filename']
        filepath = os.path.join(self.server_dir,filename)
        if os.path.isfile(filepath):
            filesize = os.path.getsize(filepath)
            head_dick['filesize'] = filesize
            head_dick_json = json.dumps(head_dick)
            head_dick_byte = head_dick_json.encode(self.coding)
            head_dick_len = len(head_dick_byte)
            head_dick_four = struct.pack('i',head_dick_len)
            self.conn.send(head_dick_four)
            self.conn.send(head_dick_byte)
            f = open(filepath,'rb')
            for line in f:
                self.conn.send(line)
            f.close()

    def ssh(self,cmd):
        os.chdir(self.server_dir)
        print("-------->%s"%cmd)
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res1 = res.stdout.read()
        res2 = res.stderr.read()
        data_size = len(res1) + len(res2)
        '''封装到报头字典'''
        head_dick = {'data_size': data_size}
        '''打包成json格式并编码'''
        head_dick_json = json.dumps(head_dick)
        head_dick_byte = head_dick_json.encode('utf8')
        '''打包字典长度固定四个字节'''
        head_pack_four = struct.pack('i', len(head_dick_byte))
        '''先发送固定4字节,在发送报头字典,最后发送数据'''
        self.conn.send(head_pack_four)
        self.conn.send(head_dick_byte)
        self.conn.send(res1)
        self.conn.send(res2)
s1=S1('127.0.0.1',10010)
s1.run()