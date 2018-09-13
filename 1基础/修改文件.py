#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import os
with open('test2','r',encoding='utf8') as f,\
    open('test_tmp','w',encoding='utf8') as g:
    for line in f:
        if line.startswith('每四年'):
            line = ''.join([line.strip(),'长亭外,古道边,芳草碧连天\n'])
        g.write(line)

os.remove('test2')
os.rename('test_tmp','test2')