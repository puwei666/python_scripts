#!usr/local/bin/python
#coding=utf-8
# by puwei666

import sys
from date_util import *

# w-覆盖；a-追加
def write_file(file_name, mode, message):
    f = open(file_name, mode)
    f.write(message)
    f.close()

# 记录日志
def write_log(file_name, message):
    f = open(file_name, 'a')
    f.write(get_current_time('%Y-%m-%d %H:%M:%S') +"\t"+ message)
    f.write('\n')
    f.close()

# 记录异常
def write_error(file_name, message):
    f = open(file_name, 'a')
    f.write(get_current_time('%Y-%m-%d %H:%M:%S')  +"\t"+ message)
    f.write('\n')
    f.close()

def send_email (send_mail, send_file) :
    os.system("sendmail -t "+ send_mail +" < "+ send_file)

# 单引号替换为两个单引号
def replace_single_quotes (strs):
    return strs.replace("'", "''")

