# -*- coding: utf-8 -*-
# from the review area
import itertools


def pi(N):
    sum_ = 0
    n1 = itertools.count(1, 2)
    n2 = itertools.cycle([4, -4])
    for x in range(N):
        sum_ += next(n2) / next(n1)
    return sum_

def pi_2(N):
    odd = itertools.count(1, 2)
    ns = list(itertools.takewhile(lambda x:x<=2*N-1, odd))
    ns1= map(lambda x:4/x if x%4 == 1 else -4/x, ns)
    return sum(ns1)
