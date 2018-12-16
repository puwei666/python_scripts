#coding=utf-8
# by puwei666

import sys, os
CURRENT_PATH = os.path.split(os.path.realpath(__file__))[0]

# 获取当前目录的上一级目录
def get_parent_dir(current_dir):
    res = ''
    dir_ary = current_dir.split('/')
    if (len(dir_ary) > 0) :
        dir_ary.pop()
        res = '/'.join(dir_ary)
    return res

common_path = get_parent_dir(CURRENT_PATH) +'/utils/'
sys.path.append(common_path)
from common import *

strs = "{'user_id':1, 'user_name':'puwei666'}"
encode_strs = base64.b64encode(strs)
print encode_strs
encode_strs = 'eyJvcGVuSWQiOiJvVGNWNjVUbnVBbmJNNTMwSWU4WUN0VTYxbnZRIiwic2NyZXdJZCI6Ind4ZjhlOTg4NmFjOTQ4MGViYSIsInVzZXJJZCI6IjQxNzhlMjMzZjYxYzQ2NTY5N2FhZGJiZTIzZWNjN2Q1In0.'
decode_strs = base64_decode(encode_strs)
print decode_strs

encode_strs = '5paw5Lqn5ZOB55qE5biC5Zy6566h55CGMWk'
decode_strs = base64.b64decode(encode_strs)
print decode_strs



