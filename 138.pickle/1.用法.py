#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

import pickle

# pickle用法跟json一样,但是支持所有的数据类型,只能在python内部进行数据交换,不能处理一个文件连续写入多个数据

def fun1():
    print("11")


a= fun1


#序列化后是bytes字节类型,需要wb写入

f = open("file1",'wb')

a1 = pickle.dumps(a)
f.write(a1)
f.close()

f1 = open("file1","rb")
c1 = pickle.loads(f1.read())
c1()
f1.close()