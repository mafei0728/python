#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
a=os.path.abspath(__file__)
b=os.path.dirname(a)
c=os.path.dirname(b)
print(c)
sys.path.append(c)