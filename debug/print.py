def foo(x):
    a = int(x)
    print('>>> a = %d' % a)
    return 10 / a


def main():
    return foo('0')


main()
