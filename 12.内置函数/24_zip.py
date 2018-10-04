#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


#11对应的迭代器.多的不要
a='12345'
b='zgfhj11'
c='121212111'
res = zip(a,b,c)
for i in res:
    print(i)

a={
    "a":111,
    "b":222,
    "c":3333,
    "d":333322,
}
res1 = zip(a.values(),a.keys())
print(max(res1)[0])

