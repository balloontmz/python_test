from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的函数代码
def write(b):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        time.sleep(random.random())  # 此方法的位置决定个别输出的顺序
        print('Put %s to queue...' % value)
        b.put(value)


# 读进程执行的函数代码
def read(b):
    print('Process to read: %s.' % os.getpid())
    while True:
        value = b.get(True)  # get的作用是区某个value并删除之
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动读写进程
    pw.start()
    pr.start()
    # 等待写进程结束
    pw.join()
    # 强制结束读进程，不然会无线循环
    pr.terminate()