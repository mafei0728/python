#!/usr/bin/env python
# -*- coding:utf-8 -*-
import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)
print(matchObj)
print(matchObj.groups()) #分组匹配放到元祖里面
print(matchObj.group())  #默认是0,打印匹配的所有字符串
if matchObj:
    print("matchObj.group(0) : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print
    "No match!!"