
# 进程间的通信及队列
# queue.Queue 进程内的非阻塞队列，不能跨进程通信
# 一般在producer 和consumer在同一个进程的时候工作
import time,random,os,queue
from multiprocessing import Process

def test(q):
    print('Process to write: {0}'.format(os.getpid()))
    for value in ['A','B','C']:
        print('Put {0} to queue...'.format(value))
        q.put(value)
        time.sleep(random.random())

    print('Process to read: {0}'.format(os.getpid()))

    while not q.empty():
        value = q.get()
        print('Get {0} from queue...'.format(value))
        time.sleep(random.random())


if __name__ == '__main__':
    q = queue.Queue()
    p = Process(target=test,args=(q,))
    p.start()
    p.join()
