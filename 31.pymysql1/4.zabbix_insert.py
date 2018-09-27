#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
import pymysql,time,random
#定义变量
host = '172.16.30.33'
user = 'root'
password = '1qaz!QAZ'
database = 'zabbix'
table = 'test01'


def time_cost(fun):
    def fun1(*args,**kwargs):
        start_time = time.time()
        res = fun()
        stop_time = time.time()
        print('cost %s'%(stop_time-start_time))
        print('qps: %s'%(100000/(stop_time-start_time)))
    return fun1




@time_cost
def insert():
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    cursor = conn.cursor()
    cursor.execute("create table if not exists test01(id int(10) unsigned zerofill auto_increment not null primary key,name varchar(5))")
    cursor.execute("truncate table test01;")
    count=0
    for k in range(100000):
        name1 = ''
        for z in range(5):
            eml=chr(random.randint(97,122))
            name1 += str(eml)
        sql ="insert into test01 (name) values (%s)"
        cursor.execute(sql,name1)
        conn.commit()
        count +=1
        count1 =0
        if count == 10000:
            count = 0
            count1 += 1
            time.sleep(1)
            print(count1)
    cursor.close()
    conn.close()


insert()