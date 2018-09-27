#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import base64,sys,cx_Oracle
'''Incoming parameters'''
#account=input("修改的账号:")
#new_password=input("修改的密码:")
account=sys.argv[1]
new_password=sys.argv[2]
#account='xmcdc'
#new_password='123456789sds'
print(account)
print(new_password)
user=''
password=''
dsn=''
'''init'''
def init(fun):
    def fun1(*args,**kwargs):
        init1=fun(*args,**kwargs)
        next(init1)
        return init1
    return fun1

@init
def gener_passwd(target):
    while True:
        new_password = yield
        new1_password = new_password.encode()
        new2_password = base64.b64encode(new1_password).decode()
        target.send(new2_password)

@init
def test():
    while True:
        new2_password = yield
        print(new2_password)


@init
def change(user,password,dns):
    while True:
        new2_password = yield
        conn = cx_Oracle.connect(user=user,password=password,dsn=dsn)
        cursor = conn.cursor()
        res = cursor.execute('update USERSPLATFORM set USPL_PASSWORD=:new2_password WHERE USPL_CODE=:account',(new2_password,account))
        conn.commit()
        #cursor.execute('select * from USERSPLATFORM')
        #res1 = cursor.fetchone()
        #print(res1)
        cursor.close()
        conn.close()
        print('账号%s修改成功,密码为%s'%(account, new_password))
hhh = gener_passwd(change(user,password,dsn))
hhh.send(new_password)

###程序打包成exe
## pyinstaller -F -w changepasword.py
