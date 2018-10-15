#!/usr/bin/env python
# -*- coding:utf-8 -*-

# cs架构

# server端

# web 7层模型
# 1:物理层(0,1的电信号)
# 2:数据链路层(以太网层协议)(mac)
# 一个数据包叫做帧,每一组数据帧分为报头head(18个字节)和数据data两部分组成
# head包含发送者/原地址 6个字节,接受者/目的地址 6个字节,数据类型 6个字节
# head长度+data长度最短是64个字节,最长是1518个字节,超过这个数字将会分片发送
# 3:网络层(ip)
# ip协议帮你找到子网
# arp协议将ip地址解析成mac地址,找到唯一的那台设备
# 4:传输层(tcp/udp)
# 通用端口找到设备上面的软件
# 5:应用层(开始跟client进行网络通信)

# client端

#http://www.cnblogs.com/linhaifeng/articles/6129246.html#_label
# socket