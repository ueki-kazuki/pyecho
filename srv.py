#!/usr/bin/env python

import socket
import threading

MSGLEN = 1024

def echo(s):
    chunks = []
    byte_recv = 0
    while byte_recv < MSGLEN:
        chunk = s.recv(min(MSGLEN - byte_recv, 2048))
        if chunk == b'':
            break
            #raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        byte_recv += len(chunk)
    message = b''.join(chunks)
    print(message)

listensocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listensocket.bind(('127.0.0.1', 18080))
listensocket.listen(3)

while True:
    (serversocket, addr) = listensocket.accept()
    client_thread = threading.Thread(name='echo-server', target=echo, args=[serversocket])
    client_thread.start()