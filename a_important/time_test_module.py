import functools,time


def log(text='run'):
    def decorator(func):
            @functools.wraps(func)
            def wrapper(*args,**kw):
                print('beginning')
                bg=time.time()
                run=func(*args,**kw)
                end=time.time()
                print('end:%2fms'%(end-bg))
                print('%s %s:'%(text,func.__name__))
                return run
            return wrapper
    return decorator

@log()
def now():
    time.sleep(0.12)


@log()
def now2():
    time.sleep(0.24)

now()
now2()


