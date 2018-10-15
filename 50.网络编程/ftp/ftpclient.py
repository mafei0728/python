#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket,os,json,struct,sys,time
class C1:
    """socket"""
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    allow_reuse_address = True
    coding = 'utf8'
    client_dir = '.'
    max_size_package = 8192
    def __init__(self,server_ip,server_port,connect=True):
        self.server_ip = server_ip
        self.server_port = server_port
        self.connect = connect
        self.socket = socket.socket(self.address_family,self.socket_type)
        if self.connect:
            try:
                self.connect_server()
            except ConnectionRefusedError:
                raise
    def connect_server(self):
        self.socket.connect((self.server_ip,self.server_port))

    def run(self):
        while True:
            put = input("ftp==>")
            if put == 'close':
                self.closed_client()
                break
            if not put:continue
            """1表示只切割一次,防止目录多个空格"""
            cmd_list = put.split(maxsplit=1)
            if len(cmd_list) == 2:
                if cmd_list[0] == 'cmd':
                    cmd = cmd_list[1]
                    fun = getattr(self,'ssh')
                    fun(cmd)
                else:
                    cmd = cmd_list[0]
                    filepath = cmd_list[1]
                    print(filepath)
                    if hasattr(self,cmd):
                        fun = getattr(self,cmd)
                        fun(filepath)
            else:
                print('上传/下载 put/get filepath\nssh命令请用cmd command')
    def put(self,filepath):
        if os.path.isfile(filepath):
            head_dick = {}
            filepath_dict = os.path.split(filepath)
            filesize = os.path.getsize(filepath)
            head_dick['filesize'] = filesize
            print(filesize)
            head_dick['filename'] = filepath_dict[1]
            head_dick['cmd'] = 'put'
            head_dick_json = json.dumps(head_dick)
            head_dick_byte = head_dick_json.encode(self.coding)
            head_dick_four = struct.pack('i',len(head_dick_byte))
            self.socket.send(head_dick_four)
            self.socket.send(head_dick_byte)
            send_size = 0
            f = open(filepath,'rb')
            for line in f:
                self.socket.send(line)
                send_size += len(line)
                percent = (send_size/filesize)*100
                print('%.2f%%' % percent)
            print('上传完成')
            f.close()
        else:
            print('文件不存在,或者没有权限')

    def get(self,filepath):
        head_dick = {}
        filename = os.path.split(filepath)[1]
        cmd = 'get'
        head_dick['filename'] = filename
        head_dick['cmd'] = cmd
        head_dick_json = json.dumps(head_dick)
        head_dick_byte = head_dick_json.encode(self.coding)
        head_dick_four = struct.pack('i',len(head_dick_byte))
        self.socket.send(head_dick_four)
        self.socket.send(head_dick_byte)
        head_pack_four = self.socket.recv(4)
        head_dick_len = struct.unpack('i', head_pack_four)[0]
        head_dick_byte = self.socket.recv(head_dick_len)
        head_dick_json = head_dick_byte.decode(self.coding)
        head_dick = json.loads(head_dick_json)
        filesize = head_dick['filesize']
        filepath =os.path.normpath(os.path.join(self.client_dir,filename))
        if os.path.isfile(filepath):
            os.remove(filepath)
        f = open(filepath, "wb")
        data_size = 0
        while filesize > data_size:
            recv_data = self.socket.recv(self.max_size_package)
            f.write(recv_data)
            data_size += len(recv_data)
            percent = (data_size / filesize) * 100
            print('%.2f%%' % percent)
        print('下载完成')
        f.close()

    def ssh(self,put):
        head_dick = {}
        cmd = put
        head_dick['cmd'] = cmd
        head_dick_json = json.dumps(head_dick)
        head_dick_byte = head_dick_json.encode(self.coding)
        head_dick_four = struct.pack('i', len(head_dick_byte))
        self.socket.send(head_dick_four)
        self.socket.send(head_dick_byte)
        head_pack_four = c1.socket.recv(4)
        head_dick_len = struct.unpack('i', head_pack_four)[0]
        '''在收报头字典'''
        head_dick_byte = c1.socket.recv(head_dick_len)
        head_dick_json = head_dick_byte.decode('utf8')
        head_dick = json.loads(head_dick_json)
        '''通过报头字典得到数据长度'''
        data_size = head_dick['data_size']
        recv_size = 0
        recv_data = b''
        '''确定收到的长度的数据才停止收包'''
        while recv_size < data_size:
            data = c1.socket.recv(1024)
            recv_size += len(data)
            recv_data += data
        print(recv_data.decode('gbk'))

    def closed_client(self):
        self.socket.close()

c1 = C1('127.0.0.1',10010)
c1.run()