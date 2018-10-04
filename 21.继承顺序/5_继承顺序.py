#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

class D(B):
    pass

class E(C):
    pass

class F(D):
    pass

class G(E):
    pass

class H(F,G):
    pass

print(H.__mro__) ##查看继承顺序
print(H.mro())

#py23新式类广度优先
#py2经典深度优先