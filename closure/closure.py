# -*- coding: utf-8 -*-
__author__ = 'tomtiddler'


def traveler():
    a = 0

    def move(step):
        c = a + step
        return c

    return move


result = traveler()
a = result(3)
b = result(5)
c = result(8)
