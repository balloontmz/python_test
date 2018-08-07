import threading

local_std = threading.local()

def process(name):
    local_std.std = name
    do_task_1()
    do_task_2()

def do_task_1():
    do_subtask_1()
    do_subtask_2()

def do_task_2():
    do_subtask_2()
    do_subtask_1()

def do_subtask_1():
    print('hello, %s (%s)\n' %
          (local_std.std, threading.currentThread().name))


def do_subtask_2():
    print('hi, %s (%s)\n' %
          (local_std.std, threading.currentThread().name))

t1 = threading.Thread(target=process, args=('bob',), name='Thread-E')
t2 = threading.Thread(target=process, args=('tom',), name='Thread-F')
t1.start()
t2.start()
t1.join()
t2.join()