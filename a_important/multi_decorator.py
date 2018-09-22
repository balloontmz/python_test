def decorator_a(func):
    print('Get in decorator_a')

    def inner_a(*args, **kwargs):
        print('Get in inner_a')
        return func(*args, **kwargs)

    return inner_a


def decorator_b(func):
    print('Get in decorator_b')

    def inner_b(*args, **kwargs):
        print('Get in inner_b')
        return func(*args, **kwargs)

    return inner_b


@decorator_b
@decorator_a
def f(x):
    print('Get in f')
    return x * 2
# 初始化的时候，先初始化a，a才能返回一个函数对象用于初始化b，否则没有对象给b去初始化。
# 初始化完成之后，返回的是一个b函数，调用b函数，才能返回a函数的调用从而完成整个装饰过程

f(1)