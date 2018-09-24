# -*- coding: utf-8 -*-
import time, functools


def metric(func,text=''):
    boo=callable(func)

    @functools.wraps(func)
    def wrapper(*args,**kw):
        print('%s'%text)
        bg=time.time()
        run=func(*args,**kw)
        print('%s executed in %s ms' % (func.__name__, 10.24))
        end=time.time()
        print('end')
        print('测试时间为%s'%(end-bg))
        return run

    def mid_metric(x):
        return metric(x,func)

    if boo is True:
        return wrapper
    else:
        return mid_metric


# 测试
@metric('woca')
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')