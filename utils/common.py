#!usr/local/bin/python
#coding=utf-8
# by puwei666

import sys, os, base64
reload(sys)
sys.setdefaultencoding('utf-8')
from date_util import *

# 当前脚本运行目录
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]

# w-覆盖；a-追加
def write_file(file_name, mode, message):
    f = open(file_name, mode)
    f.write(message)
    f.close()

# 记录日志
def write_info(message, envir):
    if envir == 1:
        print message
    file_path_info = get_parent_dir(CURRENT_PATH) + '/logs/info'
    file_path = file_path_info +'.'+ get_current_time('%Y-%m') +'.log'
    message = get_current_time('%Y-%m-%d %H:%M:%S') +'\t'+ message +'\n'
    write_file(file_path, 'a', message)

# 记录异常
def write_error(message, envir):
    if envir == 1:
        print message
    file_path_error = get_parent_dir(CURRENT_PATH) + '/logs/error'
    file_path = file_path_error +'.'+ get_current_time('%Y-%m') +'.log'
    message = get_current_time('%Y-%m-%d %H:%M:%S') +'\t'+ message +'\n'
    write_file(file_path, 'a', message)

# 发送电子邮件
def send_email (send_mail, send_file) :
    os.system("sendmail -t "+ send_mail +" < "+ send_file)

# 单引号替换为两个单引号
def replace_single_quotes (strs):
    return strs.replace("'", "''")

# 获取当前目录的上一级目录
def get_parent_dir(current_dir):
    res = ''
    dir_ary = current_dir.split('/')
    if (len(dir_ary) > 0) :
        dir_ary.pop()
        res = '/'.join(dir_ary)
    return res

# base64解码
def base64_decode(strs):
    lens = len(strs)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    strs = base64.b64decode(strs[:lenx])
    return strs


