import threading


balance = 0
lock = threading.Lock()  #

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(1000000):
        lock.acquire()  #
        try:
            change_it(n)
        finally:
            lock.release()  # lock(),acquire(),release()一套形成一个锁流程，该流程只能在一个线程内运行;这是单个的线程锁
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('cccc%s' % balance )