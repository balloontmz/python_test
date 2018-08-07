import os
import time
import random
# need to review
from multiprocessing import Process, Pool, Queue, Pipe, Lock
def f_lock(l, i):
    l.acquire()
    try:
        print('hello world', i)
    finally:
        l.release()

def pros_communication_lock():
    lock = Lock()

    for num in range(10):
        Process(target=f_lock, args=(lock, num)).start()
if __name__ == '__main__':
    # create_child_pro()
    # create_child_pro_pool()
    # pros_communication()


    # create_pro_pool()
    # pros_communication_pipe()
    pros_communication_lock()

