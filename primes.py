
def odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def not_divisible(n):
    return lambda x:x%n>0

def primes():
    yield 2
    it=odd_iter() #初始化一个数列
    while True:
        n=next(it)
        yield n
        it=filter(not_divisible(n),it)#筛选后的数列
l=[]
for x in primes():
    if x<1000:
       l.append(x)
    else:
        break
print(l)











