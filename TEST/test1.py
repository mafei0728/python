#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import re
a = "background-image: url(/media/images/index/im2.jpg);"
b  = re.search('\(.+\)',a)
c = b.group()
e = re.search('/.+jpg',c)
print(e.group())

# import re
# a = "mafei0728"
# b =re.match("^mafei",a)
# print(b)
# print(b.group()) #打印匹配的字符串
# c = re.match("^mafei\d",a) #d匹配后面的一个数字
# print(c.group())
# c = re.match("^mafei\d+",a) #d+ 匹配后面的多个数字
# print(c.group())