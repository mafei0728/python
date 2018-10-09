#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import hashlib
passwd = 'mafei0728'

#md5
m = hashlib.md5()
m.update(passwd.encode())
print(m.hexdigest())

passwd = 'mafei0728'
m1 = hashlib.md5("salt".encode()) #得到对象,参数为盐
m1.update(passwd.encode()) #计算结果
m1.update(passwd.encode()) #可以多次计算,为字符串相加的结果

print(m1.hexdigest()) #打印结果


#sha
n = hashlib.sha3_512()
n.update(passwd.encode())
print(n.hexdigest())


#所有的算法用法都一样

#实际应用
# 1:数据库密码加密(不准确),用户名和密码相对应存入数据库,每次通过指定的算法换算密码和账号对应存的相比较来校验
# 2:文件完整性验证,一行一行进行叠加update,最后得出整个文件的结果


#通过加盐来避免装库
import time
#md5
salt = time.strftime("%F %X") # 盐可以每次修改密码的时候随机生成,存到一个位置
print(salt)
m = hashlib.md5(salt.encode())  #每种算法都可以
m.update(passwd.encode())
print(m.hexdigest())
