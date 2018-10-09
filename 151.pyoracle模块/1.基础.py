#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
host = '172.16.30.14'
user = 'itpux'
password = 'itpux'
sid = 'rac11g'
import cx_Oracle

#单次执行，
def conn1(sql,*args,**kwargs):
    conn = cx_Oracle.connect('itpux/itpux@rac11g')
    cursor = conn.cursor()
    res=cursor.execute(sql, *args, **kwargs)
    conn.commit()
    #res1=cursor.fetchall()
    print(res)
    #print(res1)
    cursor.close()
    conn.close()
#x = (11,'ff11',19)
#conn1('insert into table01 values (:id,:name,:age )',x)




#多次执行增改
def conn2(sql,*args,**kwargs):
    conn = cx_Oracle.connect('itpux/itpux@rac11g')
    cursor = conn.cursor()
    cursor.execute('truncate table table01')
    res=cursor.executemany(sql, *args, **kwargs) #不返回受影响的行
    conn.commit()
    #res1=cursor.fetchall()
    print(res)
    #print(res1)
    cursor.close()
    conn.close()
a = [{"id":1,'name':'mafei1','age':17},{"id":2,'name':'mafei2','age':17},{"id":3,'name':'mafei3','age':17}]
b = [(6,'xx1',12),(7,'xx2',13)]
conn2('insert into table01 (id,name,age) values (:id,:name,:age)',a)
#conn2('insert into table01 values (:id,:name,:age)',b)

#查找
def conn3(sql,*args,**kwargs):
    conn = cx_Oracle.connect('itpux/itpux@rac11g')
    cursor = conn.cursor()
    cursor.execute(sql)
    res1=cursor.fetchall()
    print(res1)
    cursor.close()
    conn.close()
# a={"id":1}
# conn3("select * from table01 where id = {id}".format_map(a))#查找


#带执行计划的查找
def conn3(sql,*args,**kwargs):
    conn = cx_Oracle.connect('itpux/itpux@rac11g')
    cursor = conn.cursor()
    cursor.prepare(sql)
    print(cursor.statement) #要执行的语句
    cursor.execute(None, *args, **kwargs)
    res1=cursor.fetchall()
    print(res1)
    cursor.close()
    conn.close()
# a={'id':1}
# conn3("select * from table01 where id = :id",a)

# 1.有连接,就有关闭
# 2.execute sql注入的问题
# 3.增删改 conn.commit()
# 4.fetchone,fetecall()
# 5.获取插入的自增id
# 6.操作过后受影响的行数