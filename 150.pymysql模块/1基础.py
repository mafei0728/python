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
#连接
def mysql_conn(sql,*args,**kwargs):
    #连接数据库
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    #打开数据库,交给操作者
    cursor = conn.cursor()
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)
    cursor.close()
    conn.close()

#增加,修改需要commit操作
def insert():
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    # 打开数据库,交给操作者
    cursor = conn.cursor()
    cursor.execute("truncate table table01;")
    conn.commit()
    for k in range(10000):
        name1 = ''
        for z in range(5):
            eml=chr(random.randint(97,122))
            name1 += str(eml)
        sql ="insert into table01 (name) values (%s)"
        cursor.execute(sql,name1) #sql参数传递方式,不要用字符串拼接 adad' or 1=1 --sql注入
        conn.commit() #增加,修改需要commit
        time.sleep(2)
        #打开数据库,交给操作者
    cursor.close()
    conn.close()

#多次增加的方法
def mysql_conn1(sql,*args,**kwargs):
    #连接数据库
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    #打开数据库,交给操作者
    cursor = conn.cursor()  # 返回以元组为单位的列表
    res=cursor.executemany(sql,*args,**kwargs) # #返回受影响的行数
    conn.commit()
    print(res)
    cursor.close()
    conn.close()

#以列表元组或者列表字典的方式插入多列的方式多列插入
a = [{'name':'mafei1','age':17},{'name':'mafei2','age':17},{'name':'mafei3','age':17}]
b = [('mafei4',12),('mafei5',17)]
mysql_conn1('insert into table01 (name,age) values (%s,%s)',b)
mysql_conn1('insert into table01 (name,age) values (%(name)s,%(age)s)',a)

def mysql_conn2(sql, *args, **kwargs):
    # 连接数据库
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    # 打开数据库,交给操作者
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) #返回字典为元素的列表
    res1=cursor.execute(sql, *args, **kwargs) #返回受影响的行数
    conn.commit()
    print(res1)
    cursor.close()
    conn.close()

# #以字典的方式插入单列
# c = {'name':'mafei3','age':17}
# ##以元组的方式单列插入
# d =('ddsdd',1)
# mysql_conn2('insert into table01 (name,age) values (%s,%s)',d)
# mysql_conn2('insert into table01 (name,age) values (%(name)s,%(age)s)',c)
