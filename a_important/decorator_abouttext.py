def log(func,text='none'):
    if callable(func):
        def wrapper(*args,**kw):
            print('我要这铁棒有何用%s'%text)
            value=func(*args,**kw)
            print('我要这变化又如何')
            return value
        return wrapper
    else:
        def decorator(func2):
            return log(func2,func)
        return decorator


@log
def now():
    print('1')


@log('run')
def now2():
    print('2')


now()
now2()
