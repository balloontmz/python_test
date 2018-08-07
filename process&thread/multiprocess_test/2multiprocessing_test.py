from multiprocessing import Process
import os


# 子进程的执行函数
def run_proc(name):
    print('Run child process %s (%s)' % (name, os. getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getppid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('Child process end.')
