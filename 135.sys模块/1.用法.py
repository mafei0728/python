#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import sys
'''
sys.exit()
sys.version
sys.platform
sys.maxsize
'''
# #重点0指的是文件本身,多传不报错,少传报错
# a=sys.argv[0]
# b=sys.argv[1]
# c=sys.argv[2]
# print(sys.argv) # 文件和参数组成的列表
# print(a,b,c)

#环境变量
print(sys.path)
#搜索路径是先从内存里面,在从环境变量的列表从前向后,的顺序来搜索