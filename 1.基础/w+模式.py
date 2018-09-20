#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
f = open('test4','r+',encoding='utf8')
f.write('okokokok')
f.write('okokokok')
f.write('okokokok')
f.write('okokokok')
f.seek(0)
f.write('mafei0728')