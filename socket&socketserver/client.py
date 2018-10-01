#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
a test module
"""

__author__ = 'tomtiddler'


import socket

ip_port = ("127.0.0.1", 9999)

s = socket.socket()
s.connect(ip_port)

while True:
    inp = input("请输入要发送的信息： ").strip()
    if not inp:
        continue
    s.sendall(inp.encode())

    if inp == "exit":
        print("结束通信！")
        break

    server_reply = s.recv(1024).decode()
    print(server_reply)

s.close()
