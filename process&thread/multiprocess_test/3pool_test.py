from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name, end - start))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool()
    for i in range(10):
        p.apply_async(long_time_task, args=('第%s个进程' % i,))
    print('Waiting for all subprocess done...')
    p.close()  # 关闭执行完成的进程
    p.join()
    print('All subprocess done.')
# 如果你想同时启动大量的子进程，可以用进程池的方式批量创建，如下
# Pool()默认是CPU的核数，这里指定为4个，可以同时启动4个子经常，然后要等前面的执行完之后，才能执行后面的
# 调用join()之前必须调用close()，调用close()之后就不能继续添加新的Process了
# apply 执行直到前面的任务完成，apply_async() 并行执行
