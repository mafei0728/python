#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
def tali1(file_path):
    with open(file_path,'r') as f:
        f.seek(0,2)
        while True:
            line=f.readline()
            if not line:
                time.sleep(0.5)
                continue
            print(line.strip())


def tali2(file_path):
    with open(file_path,'r') as f:
        f.seek(0,2)  # 2这个参数从末尾开始
        while True:
            line=f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line.strip()

y=tali2('/root/pythontest/a.txt')
for i in y:
    print(i)


###grep到某个字符串才打印
def tali3(file_path):
    with open(file_path,'r') as f:
        f.seek(0,2)  # 2这个参数从末尾开始
        while True:
            line=f.readline()
            if not line or 'error' not in line:
                time.sleep(0.5)
                continue
            yield line.strip()

y=tali3('/root/pythontest/a.txt')
for i in y:
    print(i)

#另一种实现
def tali4(file_path):
    with open(file_path, 'r') as f:
        f.seek(0, 2)  # 2这个参数从末尾开始
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def grep(pattern,lines):
    for i in lines:
        if pattern in i:
            print(i.strip())

h = tali4('/xx/xxx')
grep('hello ,world',h)

#生产者,消费者
def tali5(file_path):
    with open(file_path, 'r') as f:
        f.seek(0, 2)  # 2这个参数从末尾开始
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            yield line

def grep1(pattern,lines):
    for i in lines:
        if pattern in i:
            yield i.strip()


h1=tali5('/root/pythontest/a.txt')
h2=grep1('error',h1)
for k in h2:
    print(k)




