def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda it: it % n > 0


def primes():
    yield 2
    it = odd_iter()  # 初始化一个数列
    while True:
        n = next(it)
        yield n
        it = filter(not_divisible(n), it)  # 筛选后的数列


list_ = []
for x in primes():
    if x < 1000:
        list_.append(x)
    else:
        break
print(list_)
