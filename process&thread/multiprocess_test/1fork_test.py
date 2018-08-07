import os,time

print('Process (%s) start...' % os.getpid())

pid = os.fork()
if pid == 0:
    print('I an child process (%s) and my parent is (%s)' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just creat a child process (%s).' % (os.getpid(), pid))

# 以下代码描述父子进程的同步执行
"""
if pid == 0:
    for i in range(100,200):
        print(i)
        time.sleep(1)
else:
    for i in range(100):
        print(i)
        time.sleep(1)
"""