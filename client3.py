# -*- coding: UTF-8 -*-
import socket

HOST = '47.105.38.117'    # The remote host
PORT = 8888  # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg = bytes(input(">>:"), encoding="utf8")
    s.sendall(msg)
    data = s.recv(1)
    # print(data)
    print('Received', repr(data))