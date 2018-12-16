# !usr/local/bin/python
# coding=utf-8
# 功能：测试date_util
# by seven

import sys
sys.path.append('xx')
from date_util import *

if __name__ == '__main__':
    '''
    s = timestamp_datetime(1332888820, '%Y-%m-%d %H:%M:%S')
    print s
    d = datetime_timestamp('2012-03-28 06:53:40')
    print d
    '''

    s = '1985-09-28 00:00:00.000000'
    d = string_date('1985-09-28 00:00:00.000000', '%Y-%m-%d %H:%M:%S')
    print d

