# !usr/local/bin/python
# coding=utf-8
# 功能：时间处理函数
# by puwei666

import time, datetime
from datetime import date

# ========== 格式转换 start ==========
# 时间的表现形式：
#   时间戳（timestamp）
#   格式化的时间字符串（str）
#   time模块的time.struct_time
#   datetime模块的datetime类

def timestamp_datetime (ts, format):
    # 经过localtime转换后变成：time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=0)
    ts = time.localtime(ts)
    # 经过strftime函数转换为正常日期格式
    dt = time.strftime(format, ts)
    return dt

def datetime_timestamp (dt, format):
    # 将字符串转化为时间数组，再转化为时间戳
    ts = time.mktime(time.strptime(dt, format))
    return int(ts)

# 功能：string 转换成 date
def string_date (s, format):
    dt = string_datetime(s, format)
    today = date.today()
    d = today.replace(year=dt.year, month=dt.month, day=dt.day)
    return d

# 功能：string 转换成 datetime
def string_datetime (s, format):
    return datetime.datetime.strptime(s, format)

# 功能：字符串转换为time类型
def string_time (s, format):
    return time.strptime(s, format)

# 功能：time类型转换为datetime类型
def time_datetime (t):
    return datetime.datetime(*t[:6])

# ========== 格式转换 end ==========

# 获取当前时间
def get_current_time (format):
    return time.strftime(format,time.localtime(time.time()))

# 功能：根据生日获取年龄
# born：生日，date类型
def calculate_age (born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:
        # 当今年不是闰年，而生日是2月29号时报错
        birthday = born.replace(year=today.year, day=born.day-1)
    age = 0
    if birthday > today:
        age = today.year - born.year - 1
    else:
        age = today.year - born.year
    if age < 0:
        age = 0
    return age

