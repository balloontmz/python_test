#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
:keyword多线程socket测试
"""

__author__ = 'tomtiddler'

import socket
import threading


def link_handler(link, client):
    """
    该函数为线程需要执行的函数负责具体的服务器和客户端之间的通信工作
    :param link: 当前线程处理的连接
    :param client: 客户端socket，一个二元数组
    :return:
    """
    print("服务器开始接收来自[{0}:{1}]的内容".format(client[0], client[1]))
    while True:
        client_data = link.recv(1024).decode()
        if client_data == "exit":
            print("服务器结束接收来自[{0}:{1}]的通信".format(client[0], client[1]))
            break
        print("服务器开始接收来自[{0}:{1}]发送了：{2}".format(client[0], client[1], client_data))
        link.sendall("服务器已经收到你的消息".encode())
    link.close()  # 关闭连接，非常需要


ip_port = ("127.0.0.1", 9999)
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.bind(ip_port)
sk.listen(5)

print("启动socket服务，等待客户端连接。。。")

while True:
    conn, address = sk.accept()  # 等待连接，此处自动阻塞 -- 对于异步请求呢
    t = threading.Thread(target=link_handler, args=(conn, address))
    t.start()  # 此处不使用join，因为在分线程执行的时候，主进程依旧需要往下执行

