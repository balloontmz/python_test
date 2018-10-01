#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
socketserver
源码并不复杂，当遇到问题时，不妨查看文档或者直接分析源码。
"""

__author__ = 'tomtiddler'

import socketserver


class MyServer(socketserver.BaseRequestHandler):
    """
    必须继承socketserver.BaseRequestHandler类
    并且实现 handle 方法
    """
    # 此函数相当于一个连接，需要长连接，所以设置无限循环，实际情况应该设置过期时间？
    def handle(self):
        conn = self.request  # 封装了request所有请求的数据
        conn.sendall("欢迎访问socketserver服务器！".encode())
        while True:
            data = conn.recv(1024).decode()
            if data == "exit":
                print("断开与{0}的连接！".format(self.client_address))
                break
            print("来自{0}发来的消息！".format(self.client_address))
            conn.sendall(("已收到妳的消息：<{0}>".format(data)).encode())


if __name__ == "__main__":
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 9999), MyServer)
    print("启动socketserver服务器！")
    server.serve_forever()
