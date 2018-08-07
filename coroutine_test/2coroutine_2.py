

def consumer():
    y = None
    while True:
        x = yield y
        if not x: # 判断是否传入了数据，（数据采用x进行接收），此句在启动器开启并调用前不会生效
            return
        print('[CONSUMER] Consuming %s...' % x)
        y = '200 OK'


def produce(z):
    z.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = z.send(n)
        print('[PRODUCER] Consumer return %s...' % r)
    z.close()


c = consumer()
produce(c)
