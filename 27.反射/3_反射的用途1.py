#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

## haproxy 中的增删改查
import sys

m1 = sys.modules[__name__]

def add_ha():
    print("add.....")

def del_ha():
    print("del......")

def search():
    print("search........")

def change():
    print("change........")


list_oper = '''
    1.add
    2.del
    3.search
    4.change
    5.quit
'''
while True:
    opr = input("---->:").strip()
    if opr == 'quit':
        break
    #print(m1.__dict__)
    if not hasattr(m1,opr):
        continue
    t1 = getattr(m1,opr)
    t1()