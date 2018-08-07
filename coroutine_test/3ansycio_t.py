# -*- coding: utf-8 -*-
import asyncio
import time, functools


def metric(func, text=''):
    boo = callable(func)

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%s' % text)
        bg = time.time()
        run = func(*args, **kw)
        end = time.time()
        print('end')
        print('测试时间为%s' % (end - bg))
        return run

    def mid_metric(x):
        return metric(x, func)

    if boo is True:
        return wrapper
    else:
        return mid_metric


@asyncio.coroutine
def hello():
    print('Hello world!')
    bg = time.time()
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    end = time.time()
    print('\nHello again!%f' % (end - bg))


# 获取EventLoop
loop = asyncio.get_event_loop()


# 执行 Coroutine
# loop.run_until_complete(hello())
# 以下装饰器显示了hello（）函数的进入次数
@metric
def te():
    return loop.run_until_complete(hello())


te()
loop.close()
