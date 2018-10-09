#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728


class List(list):
    def append(self, object): # 通过派生二次加工数据
        if not isinstance(object,int):
            raise TypeError("必须传递整数")
        super().append(object)

    def insert(self, index:int, object): #:后面是占位符,不影响,只提示
        if not isinstance(object, int):
            raise TypeError("必须传递整数")
        super().insert(index,object)

l1 = List([1,2,3,4,56])
print(l1)
l1.append(12)
print(l1)
#l1.append("sadsd")
l1.insert(1,"22")


### 但是上面只是针对了两种操作,并不影响其他list的方法