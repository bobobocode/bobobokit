#!/usr/bin/env python3


import socket


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_server(address):
    s = socket(socket.AF_INET, socket.SOCK_STREAM)
