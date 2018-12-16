#!usr/local/bin/python
#coding=utf-8

from db import *
envir = 1

def main ():
    sql = "select * from xx limit 1";
    res = execute_sql('xx', envir, sql)
    print res

if __name__ == '__main__':
    main()

