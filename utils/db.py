#!usr/local/bin/python
#coding=utf-8
# by puwei666

'''
参数envir：环境变量，1-测试环境；2-生产环境；
to do：
    1、线上环境读取配置文件
'''

import sys, MySQLdb
from common import *

read_offline_test = { 'host':'127.0.0.1', 'port':3306, 'db':'test', 'user':'test', 'passwd':'123' }
read_online_test = { 'host':'127.0.0.1', 'port':3306, 'db':'test', 'user':'test', 'passwd':'123' }
write_offline_test = { 'host':'127.0.0.1', 'port':3306, 'db':'test', 'user':'test', 'passwd':'123' }
write_online_test = { 'host':'127.0.0.1', 'port':3306, 'db':'test', 'user':'test', 'passwd':'123' }

read_config = { }
read_config.setdefault('test', { 1: read_offline_test })
read_config.setdefault('test', { 2: read_online_test })

write_config = { }
write_config.setdefault('test', { 1: write_offline_test })
write_config.setdefault('test', { 2: write_online_test })

def execute_read_sql (db_name, envir, sql):
    db = None
    try:
        db = get_read_db(db_name, envir)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
    finally:
        if db:
            db.close()
    return res

def execute_write_sql (db_name, envir, sql):
    db = None
    try:
        db = get_write_db(db_name, envir)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        res = cursor.fetchall()
    finally:
        if db:
            db.close()
    return res

def get_read_db (db_name, envir):
    config = read_config[db_name][envir]
    conn = get_conn_db(config, envir)
    return conn

def get_write_db (db_name, envir):
    config = write_config[db_name][envir]
    conn = get_conn_db(config, envir)
    return conn

def get_conn_db (config, envir):
    conn_status = True
    max_retries_count = 2   # 设置最大重试次数
    conn_retries_count = 0  # 初始重试次数
    conn_timeout = 2        # 连接超时时间为2秒
    host = config['host']
    port = config['port']
    db = config['db']
    while conn_status and conn_retries_count <= max_retries_count:
        try:
            conn = MySQLdb.connect(host=host, port=port, db=db, user=config['user'], passwd=config['passwd'], 
                charset="utf8", connect_timeout=conn_timeout)
            conn_status = False
            return conn
        except:
            conn_retries_count += 1
            write_error("connect db is error! host:"+ host +", port:"+ port +", db:"+ db +", conn_retries_count:"+ conn_retries_count, envir)
            continue
    return None

