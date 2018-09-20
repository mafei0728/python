#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


while True:
    server_inf = []
    flag = False
    you_want = input("please input:")
    with open('haproxy.cnf','r',encoding='utf8') as f:
        for line in f:
            if line.startswith('backend') and you_want in line:
                flag = True
                continue
            if line.startswith('backend') and flag:
                break
            if flag:
                server_inf.append(line.strip())
    for i in server_inf:
        print(i)

