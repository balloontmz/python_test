# -*- coding: utf-8 -*-
from functools import reduce

def qua(list):
    return reduce(lambda x,y:x*y,list)


print('3 * 5 * 7 * 9 =', qua([3, 5, 7, 9]))
if qua([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')
