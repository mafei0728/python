#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import sys,time,os

for i in range(101):
    if i == 0:
        sys.stdout.write('%s%%\n'%i)
    elif i == 100:
         sys.stdout.write("100%%    下载完成")
    else:
        sys.stdout.write('\n\n正在下载:%s%%\n'%i)
    sys.stdout.flush()
    time.sleep(1)
    os.system('cls')
