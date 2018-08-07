#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# from https://www.cnblogs.com/liuyang1987/p/6292321.html 博客园


import threading
import time


class MyThread(threading.Thread):

    def actionA(self):
        A.acquire()  # count=1
        print(self.name, "gotA", time.ctime())
        time.sleep(2)
        B.acquire()  # count=2
        print(self.name, "gotB", time.ctime())
        time.sleep(1)
        B.release()  # count=1
        A.release()  # count=0

    def actionB(self):
        B.acquire()  # count=1
        print(self.name, "gotB", time.ctime())
        time.sleep(2)
        A.acquire()  # count=2
        print(self.name, "gotA", time.ctime())
        time.sleep(1)
        A.release()  # count=1
        B.release()  # count=0

    def run(self):
        self.actionA()
        self.actionB()


if __name__ == '__main__':
    A = threading.Lock()
    B = threading.Lock()
    L = []
    for i in range(5):
        t = MyThread()
        t.start()
        L.append(t)
    for i in L:
        i.join()
    print("ending.....")
