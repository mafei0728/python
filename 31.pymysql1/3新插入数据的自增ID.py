#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import pymysql,time,random
#定义变量
host = '172.16.30.10'
user = 'root'
password = '1qaz2wsx'
database = 'test01'
table = 'table01'
#插入时候获取主键自增加的id
def mysql_conn(sql,*args,**kwargs):
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.lastrowid
    print(res)
    cursor.close()
    conn.close()
mysql_conn("insert into table01 (name,age) values ('mafei0728',19)")
