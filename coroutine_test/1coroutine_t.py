
def odd():
    print('step 1 0')
    n = yield 1
    print('step 2 %s' % n)
    n = yield(3) # yield上次返回，此次取值重新开始
    print('step 3 %s%s' % (x, n))
    yield(5)

ab=odd()
n = ab.send(None)
print(n)
for x in range(1, 3):
    n = ab.send(x)
    print(n) # generator的返回值