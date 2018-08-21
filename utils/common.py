#!usr/local/bin/python
#coding=utf-8
# by puwei666

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from date_util import *
FILE_PATH_INFO = 'logs/info'
FILE_PATH_ERROR = 'logs/error'

# w-覆盖；a-追加
def write_file(file_name, mode, message):
    f = open(file_name, mode)
    f.write(message)
    f.close()

# 记录日志
def write_info(message, envir):
    if envir == 1:
        print message
    file_path = FILE_PATH_INFO +'.'+ get_current_time('%Y-%m') +'.log'
    message = get_current_time('%Y-%m-%d %H:%M:%S') +'\t'+ message +'\n'
    write_file(file_path, 'a', message)

# 记录异常
def write_error(message, envir):
    if envir == 1:
        print message
    file_path = FILE_PATH_ERROR +'.'+ get_current_time('%Y-%m') +'.log'
    message = get_current_time('%Y-%m-%d %H:%M:%S') +'\t'+ message +'\n'
    write_file(file_path, 'a', message)

# 发送电子邮件
def send_email (send_mail, send_file) :
    os.system("sendmail -t "+ send_mail +" < "+ send_file)

# 单引号替换为两个单引号
def replace_single_quotes (strs):
    return strs.replace("'", "''")

