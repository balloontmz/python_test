# -*- coding: utf-8 -*-
from functools import reduce
import logging

def str2num(s):
    try:
        return int( s )
    except Exception as e:
        logging.exception( e )  # 并不妨碍程序继续运行
        return float( s )

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()