# -*- coding: utf-8 -*-


def createCounter():
    a=(x for x in range(1,10))
    return lambda :next(a)

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('10')
else:
    print('测试失败!')