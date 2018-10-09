#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
f=lambda x,y:x+y
print(f(1,2))


# max(iter,key=lambda )
# mix(iter,key=lambda )
# sorted(iter,key=lambda )

#比较字典,通过values来比较,是降字段变为迭代器,next往后传值,在比较,min一样
a = {"a":1,"c":4,"d":11,"e":2}
print(max(a,key=lambda i:a[i]))

#排序
print(sorted(a,key=lambda i:a[i],reverse=True))