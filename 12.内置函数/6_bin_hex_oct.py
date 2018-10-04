#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728

"""
  Return the binary representation of an integer.

  """

#10进制转化为2进制
print(bin(56))

#10进制转16进制
print(hex(1245))

#10进制转8进制
print((oct(12)))



#相互在转通过int

print(int(bin(19),2))
print(int(hex(19),16))
print(int(oct(19),8))