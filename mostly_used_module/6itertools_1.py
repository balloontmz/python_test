# -*- coding: utf-8 -*-

import itertools
'''
def pi(N):
    ns,nb=[],[]
    a = itertools.count(1, 2)
    for z in range(N):
        nb.append(4/next(a)/(-1)**(z))
    return sum(nb)
'''
def pi(N):
    ns = []
    a = itertools.count(1, 2)
    b = itertools.cycle([4,-4])
    for x in range(N):
        ns.append(next(b)/next(a))
    return sum(ns)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')