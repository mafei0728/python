#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys,os
basedir1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(basedir1)
from src import test1
test1.db()
print(test1.atm.db_path)