import os
import time
import random
# 未完成，需要review
from multiprocessing import Process, Pool, Queue, Pipe


def f_pipe(conn):
    conn.send([42, None, 'hello'])
    conn.close()


def pros_communication_pipe():
    # The Pipe() function returns a pair of connection objects connected by a pipe which
    # by default is duplex (two-way).
    # The two connection objects returned by Pipe() represent the two ends of the pipe.
    #  Each connection object has send() and recv() methods (among others).
    parent_conn, child_conn = Pipe()
    print(parent_conn, child_conn)
    p = Process(target=f_pipe, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()


if __name__ == '__main__':
    # create_child_pro()
    # create_child_pro_pool()
    # pros_communication()

    # create_pro_pool()
    pros_communication_pipe()
