import multiprocessing
import time
import random
import os
from multiprocessing import Pool


#  并行执行
def write(q):
    print('Process to write: {0}'.format(os.getpid()))
    for value in ['A','B','C']:
        print('Put {0} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: {0}'.format(os.getpid()))
    time.sleep(1)
    while True:
        # 用这种方式判断有时候会不准确
        if not q.empty():
            value = q.get(True)
            print('Get {0} from queue.'.format(value))
            time.sleep(random.random())
        else:
            break


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = Pool()
    pw = p.apply_async(write,args=(q,))
    pr = p.apply_async(read,args=(q,))
    p.close()
    p.join()