#!usr/local/bin/python
#coding=utf-8
# by puwei666

# 获取数据库链接
# 函数命名：get_[read/write]_[dbname]_db
# 参数envir_flag：环境变量，1-测试环境；2-生产环境；
# 后续：线上环境读取配置文件

import sys, MySQLdb

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

def execute_sql (db_name, envir, sql):
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

def get_read_db (db_name, envir):
    config = read_config[db_name][envir]
    db = MySQLdb.connect(host=config['host'], port=config['port'], db=config['db'], user=config['user'], passwd=config['passwd'], charset="utf8")
    return db

def get_write_db (db_name, envir):
    config = write_config[db_name][envir]
    db = MySQLdb.connect(host=config['host'], port=config['port'], db=config['db'], user=config['user'], passwd=config['passwd'], charset="utf8")
    return db


