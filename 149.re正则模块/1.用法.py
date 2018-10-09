#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import re

a = 'xsasasasds'
#取出满足要求的,放在列表里面
a1=re.findall("xs",a)






















# 匹配网址
a = 'http://www.sdd.sdsds/ds@#/sdsd23/sds232sdws'
b = re.findall("https*://\w+\.\w+\..+",a)
print(b)


########################重点############################
#容易忘记混淆的几点,?指的是前一个字符0,1个ab?c  ac abc 不能匹配abbc
#[]号内元字符为普通符号,^为取反,-,\这三个有特殊意义
#.不能匹配\n
#空白字符用\s匹配 匹配任意空白字符，等价于 [\t\n\r\f]. \S取反
# http://www.runoob.com/python/python-reg-expressions.html
#