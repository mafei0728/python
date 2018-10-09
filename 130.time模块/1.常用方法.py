#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import time

#时间戳
#时间戳就是浮点数,1970到现在的秒
print(time.time())

#时间对象
t1 = time.localtime()
t2 = time.gmtime()
print(t1)
print(t1.tm_mday)


#时间对象到字符串时间
print('时间对象到字符串时间')
print(time.strftime("%F %X",time.localtime()))
print(time.asctime(time.localtime()))
#时间戳到字符串时间
print(time.ctime(time.time()))


#字符串到时间对象
print("字符串到时间对象")
print(time.strptime("9999-02-01",'%Y-%m-%d'))



#时间对象到,时间戳
print(time.mktime(time.localtime()))


#其他常用的方法
time.sleep(1)