#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import re

a = 'xsasasasds'
#取出满足要求的,放在列表里面
a1=re.findall("xs",a)
print(a1)
























# 匹配网址
a = 'http://www.sdd.sdsds/ds@#/sdsd23/sds232sdws'
b = re.findall("https*://\w+\.\w+\..+",a)
print(b)