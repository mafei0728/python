#!/usr/bin/env python
# -*- coding:utf8 -*-
# author:mafei0728
# 日志分为五个等级,默认等级为warning,只会输出等级以上的信息
import logging,time


# # 日志基本配置
# # 1:configura 只能限制一个流(不推荐)
# logging.basicConfig(level=logging.DEBUG,
#                     format="%(asctime)s %(levelname)s [%(lineno)s] %(message)s",  # 格式化输出,参数见配置参数
#                     datefmt="%Y-%m-%d",                                            # 个数化时间
#                     filename='input.log',
#                     filemode='a',
#                     )
#
# logging.debug("ass")
# logging.info("cc")
# logging.warning("dd")
# logging.error("dsdsd")
# logging.critical("dsdsf")

def fun_logger(filepath):
    # 2:logger对象(生产中推荐使用)
    logger = logging.getLogger()
    #创建两个流对象,文件流和屏幕流,文件流还可以更改模式
    fh = logging.FileHandler("input2.log",mode='w')
    sh = logging.StreamHandler()
    #创建格式
    fm = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    #添加输出流
    logger.addHandler(fh)
    logger.addHandler(sh)
    #输出流添加格式
    fh.setFormatter(fm)
    sh.setFormatter(fm)
    #设置日志级别,默认是debug,你流对象的级别只能大于小于他,不能低于他
    logger.setLevel(logging.DEBUG)
    fh.setLevel(logging.ERROR)
    sh.setLevel(logging.ERROR)
    return logger
logger = fun_logger("xxx")

logger.debug("1.debug")
logger.info("2.info")
logger.warning("3.warning")
logger.error("4.error")
logger.critical("5.critical")