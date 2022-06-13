#!/usr/bin/env python3

from collections import deque
from select import select
from socket import *
import pdb

tasks = deque()
recv_wait = {}
send_wait = {}


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            # No active tasks to run
            # wait for I/O
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
            why, what = next(task)
            if why == "recv":
                # Must go wait somewhere
                recv_wait[what] = task
            elif why == "send":
                send_wait[what] = task
            else:
                raise RuntimeError("ARG!")
        except StopIteration:
            print("task done")


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        yield "recv", sock
        client, addr = sock.accept()
        print("Connection", addr)
        tasks.append(fib_handler(client))


def fib_handler(client):
    while True:
        yield "recv", client
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        result = fib(n)
        result = b"fib: " + str(result).encode("ascii") + b"\n"
        yield "send", client
        client.send(result)
    print("Closed")


pdb.set_trace()
tasks.append(fib_server(('', 8080)))
run()
