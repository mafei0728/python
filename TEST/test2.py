#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import pymysql
host = '172.16.30.10'
user = 'root'
password = '1qaz2wsx'
database = 'test01'
table = 'table01'

# 连接数据库
conn = pymysql.connect(host=host, user=user, password=password, database=database)
# 打开数据库,交给操作者
c = {'name':'mafei3','age':17}
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) #返回字典为元素的列表
res1=cursor.execute("insert into table01 (name,age) values (%(name)s,%(age)s)",c)
conn.commit()
print(res1)
cursor.close()
conn.close()
