#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'

import time
import functools


def metric(func, text=''):
    boo = callable(func)

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s' % text if text else "\nbegin")
        bg = time.time()
        run = func(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (func.__name__, end - bg))
        print('end\n')
        return run

    def mid_metric(x):
        return metric(x, func)

    if boo is True:
        return wrapper
    else:
        return mid_metric
