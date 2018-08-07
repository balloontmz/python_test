import threading

def process(name):
    std = name
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_1(std)

def do_subtask_1(std):
    print('hello, %s (%s)\n' % (std, threading.currentThread().name))


def do_subtask_2(std):
    print('hi, %s (%s)\n' % (std, threading.currentThread().name))

t1 = threading.Thread(target=process, args=('bob',), name='Thread-A')
t2 = threading.Thread(target=process, args=('tom',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
