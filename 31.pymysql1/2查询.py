#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import pymysql
host = '172.16.30.10'
user = 'root'
password = '1qaz2wsx'
database = 'test01'
table = 'table01'


#一条一条取
def mysql_conn1(sql,*args,**kwargs):
    #连接数据库
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    #打开数据库,交给操作者
    cursor = conn.cursor()  # 返回以元组为单位的列表
    cursor.execute(sql,*args,**kwargs)
    #一次取一行,跟readline相似,光标下移
    res = cursor.fetchone()
    print(res)
    res = cursor.fetchone()
    print(res)
    res = cursor.fetchone()
    print(res)
    #光标自定移动,类似seek
    cursor.scroll(1,mode='relative') #相对当前位置
    cursor.scroll(2,mode='absolute') #相对绝对位置
    cursor.close()
    conn.close()

#手动控制拿的数据
def mysql_conn2(sql,*args,**kwargs):
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    #打开数据库,交给操作者
    cursor = conn.cursor()  # 返回以元组为单位的列表
    cursor.execute(sql,*args,**kwargs)
    #一次取N条数据,这个用的少,光标下移
    res = cursor.fetchmany(4)
    print(res)
    cursor.close()
    conn.close()

#拿所有数据,分页显示,用limit控制
def mysql_conn15(sql,*args,**kwargs):
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    #打开数据库,交给操作者
    cursor = conn.cursor()  # 返回以元组为单位的列表
    cursor.execute(sql,*args,**kwargs)
    #一次取N条数据,这个用的少,光标下移
    res = cursor.fetchall()
    print(res)
    cursor.close()
    conn.close()

#控制取出数据的格式以字典为元素的列表
def mysql_conn4(sql,*args,**kwargs):
    conn = pymysql.connect(host=host,user=user,password=password,database=database)
    #打开数据库,交给操作者,
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    res1=cursor.execute(sql,*args,**kwargs) #执行会返回受影响的行数包含增删查改
    print(res1)
    res = cursor.fetchall()
    print(res)
    cursor.close()
    conn.close()

#mysql_conn4('select * from test01.table01 where id<10')


#knowledge point
def know_point():
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    cursor.fetchall()
    cursor.fetchmany()
    cursor.fetchone()
    cursor.scroll(1,mode='relative')
    cursor.scroll(2,mode='absolute')






