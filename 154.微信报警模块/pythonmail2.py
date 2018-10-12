#!/usr/bin/python
# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import sys

#smtpaddr = 'smtp.qq.com'
smtpaddr = 'smtp.qq.com'
myemail='3381523702@qq.com'
password='sbflqxzwgjiucibi'
#f = open('/usr/local/zabbix/alertscripts/password','r')
#password = f.readline()

recvmail=sys.argv[1]
subject=sys.argv[2]
content=sys.argv[3]

msg = MIMEText("""%s"""%(content), "plain", "utf-8")

msg['Subject'] = Header(subject, 'utf-8').encode()
msg['From'] = myemail
msg['To'] =  recvmail

try:
        server = smtplib.SMTP()
        server.connect(smtpaddr, "25")
        server.starttls()
        server.login(myemail, password)
        server.sendmail(myemail, recvmail.split(','), msg.as_string())
        server.quit()
        print("success")
except Exception as e:
        print("fail: "+str(e))
