# -*- coding:utf-8 -*-
from datetime import datetime, timedelta, timezone
import re

# 慌慌张张，匆匆忙忙。
def to_timestamp(dt_str, tz_str):
    dt_time = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    reg = re.compile(r'^(UTC)([\+\-])([0-9]+?)\:([0-9]+)$')
    if reg.match(tz_str):
        b = int(reg.match(tz_str).group(3))
        dt_utc = dt_time.replace(tzinfo=timezone(timedelta(hours=b if reg.match(tz_str).group(2) == '+' else -b)))
        # 强行加上时区，简化的内部循环
        utc_time = dt_utc.astimezone(timezone.utc)
        # 将时区转换为初始时区
        print('%s,tomtom'%datetime.timestamp(utc_time))
        return datetime.timestamp(utc_time)
    '''
            if reg.match(tz_str).group(2) == '+':
            else:
                dt_utc = dt_time.replace(tzinfo=timezone(timedelta(hours=-b)))       
    '''

# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')