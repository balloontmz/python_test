import threading
import time, random
# 此段代码表示线程并不一定按照顺序执行，而是抢占式的


class myThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    def run(self):
        print('开启线程： ' + self.name)
        # 获取锁，用于线程同步
        threadLock.acquire()
        print_time(self.name, 4)
        # 释放锁，开启下一个线程
        threadLock.release()


def print_time(threadName, counter):
    while counter:
        time.sleep(0.1)
        # 打印时间
        print('%s :%s' % (threadName, time.ctime((time.time()))))
        counter -= 1


threadLock = threading.Lock()
threads = []
th_name = ['Thread-1', 'Thread-2', 'Thread-3', 'Thread-4', 'Thread-5', 'Thread-6', 'Thread-7', 'Thread-8']
# 创建新线程
for i, n in zip(range(1, 9), th_name):
    t = myThread(i, n)
    t.start()
    threads.append(t)

# 开启新线程
for t in threads:
    t.join()
