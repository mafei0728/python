#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import sys,time,os
print("开始下载")
for i in range(101):
    sys.stdout.write('\r-%s*%s%%'%('-'*i,i))
    sys.stdout.flush()
    time.sleep(0.2)
print('\n下载完成')