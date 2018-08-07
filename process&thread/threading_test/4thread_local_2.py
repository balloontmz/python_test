import threading

globals_dict = {}

def process(name):
    globals_dict[threading.currentThread().name] = name
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
          (globals_dict[threading.currentThread().name], threading.currentThread().name))


def do_subtask_2():
    print('hi, %s (%s)\n' %
          (globals_dict[threading.currentThread().name], threading.currentThread().name))

t1 = threading.Thread(target=process, args=('bob',), name='Thread-A')
t2 = threading.Thread(target=process, args=('tom',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()