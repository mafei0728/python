#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time
print(time.time())
print(time.strftime('%Y-%m-%d %H:%M:%S'))
print(time.strftime('%F %X'),time.localtime(time.time()))
print(time.localtime(12121212121))
time.strptime('19221222','%Y%m%d')