#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
f = open('test1','a+',encoding='utf8')
f.write('\nmafei0728')
f.seek(0)
f.write('\nmafei0729')
