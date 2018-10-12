# mafei0728
#!/usr/bin/env python
# encoding: utf-8

import sys
import smtplib
import email.mime.multipart
import email.mime.text

def send_email():
    """
    发送邮件
    :param SMTP_host: smtp.163.com
    :param from_addr: 发送地址：xxx@163.com
    :param password: 密码: password
    :param to_addrs: 发送给谁的邮箱： xxx@qq.com
    :param subject:  邮件主题： test
    :param content:  邮件内容： test
    :return: None
   """
    SMTP_host = 'smtp.qq.com'
    from_addr = '3381523702@qq.com'
    password = 'sbflqxzwgjiucibi'
    to_addrs = sys.argv[1]
    subject = sys.argv[2]
    content = sys.argv[3]
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = from_addr
    msg['to'] = to_addrs
    msg['subject'] = subject
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    try:
        smtp = smtplib.SMTP()
        smtp.connect(SMTP_host, '25')
        smtp.login(from_addr, password)
        smtp.sendmail(from_addr, to_addrs, str(msg))
        smtp.quit()
        print("发送成功")
    except Exception as e:
        print("仔细阅读"+"e")
send_email()