# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
# 常见的python错误类型官方文档
x = input('x=')
choose = input('the error1 or the error2:')

def error1():
    try:
        print('trying...')
        result = 10 / int(x)
        print('result:', result)
    except ValueError as e:  # 进阶版 try...except...机制
        print('except1:', e)
    except ZeroDivisionError as a:
        print('except:', a)
    else:
        print('no error')
    finally:
        print('finally...')
    print('END')  # 忘记加了

def error2():

    def foo(b):
        return 10/int(b)

    def bar(a):
        return 2*foo(a)

    def main(x):
        try:
            print('tring...')
            print('result:', bar(x))
        except Exception as e:
            print('error:',e)
        else:
            print('no error')
        finally:
            print('finally...')
        print('end')
    main(x)

if int(choose) == 1:
    error1()
else:
    error2()