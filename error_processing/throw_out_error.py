# err_reraise.py

def foo(s):
    n = int(s)
    if n==0:
        raise ZeroDivisionError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ZeroDivisionError as e:
        print('ValueError!')
        raise   # ZeroDivisionError('111') #将内层已有的错误信息抛出外层进行处理

bar()