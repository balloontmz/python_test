from multiprocessing import Process, Queue
import os
import time
import random
# from the review area


def w(q):
    print('from subprocess w:%s of process main:%s ' % (os.getpid(), os.getppid()))
    time.sleep(1)  # 解决显示同步的问题
    for value in range(10):
        print('put ', value)
        q.put(value)
        time.sleep(random.random())
    q.put('exit')  # 退出机制，利用queue的进程间通信


def r(q):
    print('from subprocess r:%s of process main:%s ' % (os.getpid(), os.getppid()))
    while True:
        value = q.get(True)
        print('Child subprocess %s ' % value)
        if value == 'exit':
            break


if __name__ == '__main__':
    p = Queue()
    pw = Process(target=w, args=(p,))
    pr = Process(target=r, args=(p,))
    pw.start()
    pr.start()
    print('process main: ', os.getpid())
    while True:
        value_m = p.get(True)  # 进程间通信，put,get成对出现
        p.put(value_m)
        print('get %s from queue.' % value_m)
        if value_m == 'exit':
            break
    pw.join()
    pr.join()
    print('Done')
