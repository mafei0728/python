#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
from urllib.request import urlopen
#爬一个网页
def fun1(url):
    def fun2():
        print(urlopen(url).read())
    return fun2

f1 = fun1('http://www.baidu.com')
#f1就是一个人闭包,只有一个功能,就是爬百度的网页,
#也称为惰性计算,对于使用者完全透明
print(f1.__closure__[0].cell_contents)